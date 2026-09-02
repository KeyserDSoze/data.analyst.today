from __future__ import annotations

from io import BytesIO
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

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
    """Center the title page and embed editorial metadata in the DOCX."""
    doc = Document(str(path))
    nonempty = [paragraph for paragraph in doc.paragraphs if paragraph.text.strip()]

    title = str(config.get("title", "")).strip()
    subtitle = str(config.get("subtitle", "")).strip()
    author = str(config.get("author", "")).strip()

    doc.core_properties.title = title
    doc.core_properties.subject = subtitle
    doc.core_properties.author = author
    doc.core_properties.last_modified_by = author

    if nonempty:
        nonempty[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        nonempty[0].paragraph_format.space_before = Pt(80)
        nonempty[0].paragraph_format.space_after = Pt(20)

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


def polish_pdf_title_page(path: Path, config: dict) -> None:
    """Center subtitle/author on the PDF title page without rebuilding the body."""
    reader = PdfReader(str(path))
    if not reader.pages:
        return

    page = reader.pages[0]
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    subtitle = str(config.get("subtitle", "")).strip()
    author = str(config.get("author", "")).strip()

    buffer = BytesIO()
    overlay_canvas = canvas.Canvas(buffer, pagesize=(width, height))

    # Cover the original left-aligned subtitle/author block while leaving the
    # large title untouched, then redraw a cleaner centered composition.
    overlay_canvas.setFillColorRGB(1, 1, 1)
    overlay_canvas.rect(0, height * 0.742, width, height * 0.131, stroke=0, fill=1)

    if subtitle:
        overlay_canvas.setFillColor(build.colors.HexColor(f"#{ACCENT}"))
        overlay_canvas.setFont("Helvetica-Oblique", 13)
        overlay_canvas.drawCentredString(width / 2, height * 0.836, subtitle)

    if author:
        overlay_canvas.setFillColorRGB(0.12, 0.14, 0.16)
        overlay_canvas.setFont("Helvetica", 10.5)
        overlay_canvas.drawCentredString(width / 2, height * 0.805, author)

    overlay_canvas.setStrokeColor(build.colors.HexColor("#9BAAC0"))
    overlay_canvas.setLineWidth(0.7)
    overlay_canvas.line(width / 2 - 80, height * 0.780, width / 2 + 80, height * 0.780)
    overlay_canvas.save()
    buffer.seek(0)

    overlay_page = PdfReader(buffer).pages[0]
    writer = PdfWriter(clone_from=reader)
    writer.pages[0].merge_page(overlay_page, over=True)

    temp_path = path.with_suffix(".styled.pdf")
    with temp_path.open("wb") as handle:
        writer.write(handle)
    temp_path.replace(path)


def main() -> None:
    build.configure_docx_styles = configure_docx_styles
    build.pdf_styles = pdf_styles
    build.main()

    config = build.load_config()
    basename = config.get("output_basename", "book")
    polish_docx_title_page(build.BUILD_DIR / f"{basename}.docx", config)
    polish_pdf_title_page(build.BUILD_DIR / f"{basename}.pdf", config)


if __name__ == "__main__":
    main()
