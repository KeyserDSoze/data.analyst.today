from __future__ import annotations

import re
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from ebooklib import epub
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
CONFIG_PATH = ROOT / "book.yml"
SECTION_HEADING_RE = re.compile(r"^\d+\.\d+(?:\s|\b)")

EPUB_CSS = """
body {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.58;
  margin: 6%;
  color: #20252b;
}
h1 {
  font-size: 2.2em;
  line-height: 1.12;
  color: #1f365c;
  margin-top: 1.35em;
  margin-bottom: 0.8em;
  padding-bottom: 0.35em;
  border-bottom: 0.12em solid #1f365c;
  break-before: page;
  page-break-before: always;
}
h2 {
  font-size: 1.45em;
  line-height: 1.22;
  color: #1f365c;
  margin-top: 1.5em;
  margin-bottom: 0.55em;
}
h3 {
  font-size: 1.18em;
  line-height: 1.25;
  color: #1f365c;
  margin-top: 1.25em;
  margin-bottom: 0.45em;
}
p {
  margin-top: 0;
  margin-bottom: 0.85em;
}
pre, code {
  font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
}
pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  padding: 0.85em;
  background: #f4f6f8;
  border-left: 0.22em solid #1f365c;
}
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.9em;
  margin: 1em 0 1.25em 0;
}
th, td {
  border: 1px solid #aeb5bd;
  padding: 0.4em;
  vertical-align: top;
}
th {
  background: #eef2f6;
}
blockquote {
  margin-left: 0.5em;
  margin-right: 0;
  padding: 0.25em 0 0.25em 1em;
  border-left: 0.22em solid #1f365c;
}
a {
  color: #1f365c;
  overflow-wrap: anywhere;
}
""".strip()


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def markdown_parser() -> MarkdownIt:
    return MarkdownIt("commonmark").enable("table")


def inline_plain(token) -> str:
    if not getattr(token, "children", None):
        return token.content

    parts: list[str] = []
    for child in token.children:
        if child.type in {"text", "code_inline", "html_inline"}:
            parts.append(child.content)
        elif child.type in {"softbreak", "hardbreak"}:
            parts.append("\n")
        elif child.type == "image":
            parts.append(child.content or child.attrGet("alt") or "")
    return "".join(parts)


def is_top_level_h1(title: str) -> bool:
    # Keep the same protection used by the PDF/DOCX renderer: legacy section
    # headings such as "14.8 ..." must not become separate EPUB documents.
    return SECTION_HEADING_RE.match(title.strip()) is None


def split_sections(markdown: str) -> list[tuple[str, str]]:
    lines = markdown.splitlines()
    tokens = markdown_parser().parse(markdown)
    headings: list[tuple[int, str]] = []

    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag != "h1" or not token.map:
            continue
        title = inline_plain(tokens[index + 1]).strip()
        if is_top_level_h1(title):
            headings.append((token.map[0], title))

    if not headings:
        raise ValueError("EPUB: nessun H1 top-level trovato nel Markdown assemblato.")

    sections: list[tuple[str, str]] = []
    for index, (start_line, title) in enumerate(headings):
        end_line = headings[index + 1][0] if index + 1 < len(headings) else len(lines)
        body = "\n".join(lines[start_line + 1 : end_line]).strip()
        sections.append((title, body))
    return sections


def build_epub(markdown: str, output: Path, config: dict) -> int:
    parser = markdown_parser()
    sections = split_sections(markdown)

    book = epub.EpubBook()
    book.set_identifier(config.get("output_basename", "data-analyst-today"))
    book.set_title(config["title"])
    book.set_language(config.get("language", "it-IT"))
    if config.get("author"):
        book.add_author(config["author"])

    stylesheet = epub.EpubItem(
        uid="book-style",
        file_name="styles/book.css",
        media_type="text/css",
        content=EPUB_CSS,
    )
    book.add_item(stylesheet)

    documents: list[epub.EpubHtml] = []
    for index, (title, body) in enumerate(sections, start=1):
        document = epub.EpubHtml(
            title=title,
            file_name=f"section-{index:03d}.xhtml",
            lang=config.get("language", "it-IT"),
        )
        rendered_body = parser.render(body) if body else ""
        document.content = f"<h1>{escape(title)}</h1>\n{rendered_body}"
        document.add_item(stylesheet)
        book.add_item(document)
        documents.append(document)

    book.toc = tuple(documents)
    book.spine = ["nav", *documents]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub(str(output), book)
    return len(documents)


def main() -> None:
    config = load_config()
    basename = config.get("output_basename", "data-analyst-today")
    markdown_path = BUILD_DIR / f"{basename}.md"
    output_path = BUILD_DIR / f"{basename}.epub"

    if not markdown_path.exists():
        raise SystemExit(
            f"Markdown assemblato non trovato: {markdown_path.relative_to(ROOT)}. "
            "Eseguire prima scripts/build.py."
        )

    markdown = markdown_path.read_text(encoding="utf-8")
    document_count = build_epub(markdown, output_path, config)
    print(
        f"EPUB completato con {document_count} documenti: "
        f"{output_path.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
