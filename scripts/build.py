from __future__ import annotations

import re
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from markdown_it import MarkdownIt
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
BUILD_DIR = ROOT / "build"
CONFIG_PATH = ROOT / "book.yml"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def numeric_prefix(path: Path) -> int:
    match = re.match(r"(\d+)", path.name)
    return int(match.group(1)) if match else 10**9


def source_files() -> list[Path]:
    chapters = sorted(
        [p for p in CHAPTERS_DIR.iterdir() if p.is_dir() and p.name.endswith("_chapter")],
        key=numeric_prefix,
    )
    files: list[Path] = []
    for chapter in chapters:
        files.extend(sorted(chapter.glob("*.md"), key=numeric_prefix))
    return files


def assemble_markdown(config: dict, files: list[Path]) -> str:
    front = (
        f"# {config['title']}\n\n"
        f"## {config.get('subtitle', '')}\n\n"
        f"**Autore:** {config.get('author', '')}\n\n"
        "---\n\n"
    )
    chunks = [front]
    for path in files:
        chunks.append(path.read_text(encoding="utf-8").strip() + "\n\n")
    return "".join(chunks)


def configure_docx_styles(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    for name, size in [("Title", 28), ("Heading 1", 22), ("Heading 2", 17), ("Heading 3", 14)]:
        style = doc.styles[name]
        style.font.name = "Aptos Display"
        style.font.size = Pt(size)

    section = doc.sections[0]
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)


def inline_text(token) -> str:
    if not getattr(token, "children", None):
        return token.content
    return "".join(child.content for child in token.children if child.type in {"text", "code_inline"})


def build_docx(markdown: str, output: Path, config: dict) -> None:
    md = MarkdownIt("commonmark")
    tokens = md.parse(markdown)
    doc = Document()
    configure_docx_styles(doc)

    i = 0
    first_h1 = True
    list_stack: list[str] = []

    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            level = int(token.tag[1])
            content = inline_text(tokens[i + 1])
            if first_h1:
                p = doc.add_paragraph()
                p.style = doc.styles["Title"]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run(content)
                first_h1 = False
            else:
                doc.add_heading(content, level=min(level, 3))
            i += 3
            continue

        if token.type == "paragraph_open":
            content = inline_text(tokens[i + 1])
            style = None
            if list_stack:
                style = "List Bullet" if list_stack[-1] == "bullet" else "List Number"
            p = doc.add_paragraph(style=style)
            p.add_run(content)
            i += 3
            continue

        if token.type == "blockquote_open":
            if i + 2 < len(tokens) and tokens[i + 1].type == "paragraph_open":
                content = inline_text(tokens[i + 2])
                p = doc.add_paragraph()
                p.style = doc.styles["Quote"]
                p.add_run(content)
            i += 1
            continue

        if token.type == "bullet_list_open":
            list_stack.append("bullet")
        elif token.type == "ordered_list_open":
            list_stack.append("number")
        elif token.type in {"bullet_list_close", "ordered_list_close"} and list_stack:
            list_stack.pop()
        elif token.type == "fence":
            p = doc.add_paragraph()
            run = p.add_run(token.content.rstrip())
            run.font.name = "Courier New"
            run.font.size = Pt(9)
        elif token.type == "hr":
            doc.add_page_break()

        i += 1

    footer = doc.sections[0].footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run(config["title"])
    doc.save(output)


def pdf_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BookTitle", parent=styles["Title"], fontSize=26, leading=31, alignment=TA_CENTER, spaceAfter=12))
    styles.add(ParagraphStyle(name="H1Book", parent=styles["Heading1"], fontSize=20, leading=24, spaceBefore=14, spaceAfter=10))
    styles.add(ParagraphStyle(name="H2Book", parent=styles["Heading2"], fontSize=15, leading=19, spaceBefore=12, spaceAfter=8))
    styles.add(ParagraphStyle(name="H3Book", parent=styles["Heading3"], fontSize=12.5, leading=16, spaceBefore=10, spaceAfter=6))
    styles.add(ParagraphStyle(name="BodyBook", parent=styles["BodyText"], fontSize=10.5, leading=15, spaceAfter=7))
    styles.add(ParagraphStyle(name="QuoteBook", parent=styles["BodyText"], fontSize=10.5, leading=15, leftIndent=12*mm, rightIndent=7*mm, spaceAfter=8))
    return styles


def build_pdf(markdown: str, output: Path, config: dict) -> None:
    md = MarkdownIt("commonmark")
    tokens = md.parse(markdown)
    styles = pdf_styles()
    story = []
    i = 0
    first_h1 = True
    list_stack: list[str] = []
    list_counter = 0

    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            level = int(token.tag[1])
            content = escape(inline_text(tokens[i + 1]))
            if first_h1:
                story.append(Paragraph(content, styles["BookTitle"]))
                first_h1 = False
            elif level == 1:
                story.append(PageBreak())
                story.append(Paragraph(content, styles["H1Book"]))
            elif level == 2:
                story.append(Paragraph(content, styles["H2Book"]))
            else:
                story.append(Paragraph(content, styles["H3Book"]))
            i += 3
            continue

        if token.type == "paragraph_open":
            content = escape(inline_text(tokens[i + 1]))
            if list_stack:
                if list_stack[-1] == "bullet":
                    content = "&#8226; " + content
                else:
                    list_counter += 1
                    content = f"{list_counter}. " + content
            story.append(Paragraph(content, styles["BodyBook"]))
            i += 3
            continue

        if token.type == "blockquote_open" and i + 2 < len(tokens) and tokens[i + 1].type == "paragraph_open":
            content = escape(inline_text(tokens[i + 2]))
            story.append(Paragraph(content, styles["QuoteBook"]))
        elif token.type == "bullet_list_open":
            list_stack.append("bullet")
        elif token.type == "ordered_list_open":
            list_stack.append("number")
            list_counter = 0
        elif token.type in {"bullet_list_close", "ordered_list_close"} and list_stack:
            list_stack.pop()
        elif token.type == "fence":
            story.append(Preformatted(token.content.rstrip(), styles["Code"]))
            story.append(Spacer(1, 5))
        elif token.type == "hr":
            story.append(PageBreak())

        i += 1

    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawCentredString(A4[0] / 2, 12 * mm, str(doc.page))
        canvas.restoreState()

    pdf = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=20*mm,
        leftMargin=20*mm,
        topMargin=20*mm,
        bottomMargin=20*mm,
        title=config["title"],
        author=config.get("author", ""),
    )
    pdf.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


def main() -> None:
    config = load_config()
    files = source_files()
    if not files:
        raise SystemExit("Nessun file Markdown trovato in chapters/.")

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    basename = config.get("output_basename", "book")
    markdown = assemble_markdown(config, files)

    md_path = BUILD_DIR / f"{basename}.md"
    docx_path = BUILD_DIR / f"{basename}.docx"
    pdf_path = BUILD_DIR / f"{basename}.pdf"

    md_path.write_text(markdown, encoding="utf-8")
    build_docx(markdown, docx_path, config)
    build_pdf(markdown, pdf_path, config)

    print(f"Build completata con {len(files)} file sorgente:")
    print(f"- {md_path.relative_to(ROOT)}")
    print(f"- {docx_path.relative_to(ROOT)}")
    print(f"- {pdf_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
