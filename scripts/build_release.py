from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

import build


ACCENT = "1F365C"
ACCENT_RGB = RGBColor(0x1F, 0x36, 0x5C)


_original_configure_docx_styles = build.configure_docx_styles
_original_pdf_styles = build.pdf_styles


def configure_docx_styles(doc: Document) -> None:
    """Apply a stronger editorial hierarchy without changing the renderer."""
    _original_configure_docx_styles(doc)

    title = doc.styles["Title"]
    title.font.size = Pt(34)
    title.font.bold = True
    title.font.color.rgb = ACCENT_RGB
    title.paragraph_format.space_after = Pt(18)

    heading1 = doc.styles["Heading 1"]
    heading1.font.size = Pt(28)
    heading1.font.bold = True
    heading1.font.color.rgb = ACCENT_RGB
    heading1.paragraph_format.space_before = Pt(28)
    heading1.paragraph_format.space_after = Pt(16)
    heading1.paragraph_format.keep_with_next = True

    heading2 = doc.styles["Heading 2"]
    heading2.font.size = Pt(18)
    heading2.font.bold = True
    heading2.font.color.rgb = ACCENT_RGB
    heading2.paragraph_format.space_before = Pt(18)
    heading2.paragraph_format.space_after = Pt(9)
    heading2.paragraph_format.keep_with_next = True

    heading3 = doc.styles["Heading 3"]
    heading3.font.size = Pt(14)
    heading3.font.bold = True
    heading3.font.color.rgb = ACCENT_RGB
    heading3.paragraph_format.space_before = Pt(13)
    heading3.paragraph_format.space_after = Pt(6)
    heading3.paragraph_format.keep_with_next = True


def pdf_styles():
    styles = _original_pdf_styles()

    styles["BookTitle"].fontSize = 32
    styles["BookTitle"].leading = 38
    styles["BookTitle"].spaceAfter = 18
    styles["BookTitle"].textColor = build.colors.HexColor(f"#{ACCENT}")

    styles["H1Book"].fontSize = 26
    styles["H1Book"].leading = 31
    styles["H1Book"].spaceBefore = 24
    styles["H1Book"].spaceAfter = 18
    styles["H1Book"].textColor = build.colors.HexColor(f"#{ACCENT}")
    styles["H1Book"].keepWithNext = True

    styles["H2Book"].fontSize = 16.5
    styles["H2Book"].leading = 20
    styles["H2Book"].spaceBefore = 16
    styles["H2Book"].spaceAfter = 9
    styles["H2Book"].textColor = build.colors.HexColor(f"#{ACCENT}")
    styles["H2Book"].keepWithNext = True

    styles["H3Book"].fontSize = 13
    styles["H3Book"].leading = 16.5
    styles["H3Book"].spaceBefore = 11
    styles["H3Book"].spaceAfter = 6
    styles["H3Book"].textColor = build.colors.HexColor(f"#{ACCENT}")
    styles["H3Book"].keepWithNext = True

    return styles


def polish_docx_title_page(path: Path, config: dict) -> None:
    """Center and space the title-page subtitle and author in the DOCX."""
    doc = Document(str(path))
    nonempty = [paragraph for paragraph in doc.paragraphs if paragraph.text.strip()]

    if nonempty:
        nonempty[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        nonempty[0].paragraph_format.space_before = Pt(80)
        nonempty[0].paragraph_format.space_after = Pt(20)

    subtitle = str(config.get("subtitle", "")).strip()
    author = str(config.get("author", "")).strip()

    for paragraph in nonempty[:8]:
        text = paragraph.text.strip()
        if subtitle and text == subtitle:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_after = Pt(18)
            for run in paragraph.runs:
                run.font.size = Pt(17)
                run.font.italic = True
                run.font.color.rgb = ACCENT_RGB
        elif author and text == f"Autore: {author}":
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_before = Pt(8)
            paragraph.paragraph_format.space_after = Pt(18)
            for run in paragraph.runs:
                run.font.size = Pt(12.5)

    doc.save(str(path))


def main() -> None:
    build.configure_docx_styles = configure_docx_styles
    build.pdf_styles = pdf_styles
    build.main()

    config = build.load_config()
    basename = config.get("output_basename", "book")
    polish_docx_title_page(build.BUILD_DIR / f"{basename}.docx", config)


if __name__ == "__main__":
    main()
