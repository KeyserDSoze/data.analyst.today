from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
PREFIX_RE = re.compile(r"^(\d+)")
SECTION_RE = re.compile(r"^#{1,6}\s+(\d+)\.(\d+)\b")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|TBD)\b", re.IGNORECASE)
WORD_RE = re.compile(r"\b[\wÀ-ÖØ-öø-ÿ’'-]+\b", re.UNICODE)
URL_RE = re.compile(r"https?://[^\s)>]+")
DISPLAY_MATH_RE = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
LATEX_COMMAND_RE = re.compile(r"\\(?:frac|sqrt|sum|prod|int|alpha|beta|sigma|mu|theta|hat|bar)\b")
ASCII_ACCENT_RE = re.compile(
    r"(?<!\w)(?:e'|piu'|puo'|cosi'|perche'|gia'|pero'|qualita'|attivita'|realta'|probabilita'|modalita'|unita'|societa')(?!\w)",
    re.IGNORECASE,
)


def prefix(path: Path) -> int:
    match = PREFIX_RE.match(path.name)
    return int(match.group(1)) if match else 10**9


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ""


def numbered_sections(text: str, chapter_num: int) -> list[int]:
    pattern = re.compile(rf"^#{{2,6}}\s+{chapter_num}\.(\d+)\b", re.MULTILINE)
    return [int(value) for value in pattern.findall(text)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Controlla struttura e convenzioni del libro.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Tratta anche i warning editoriali come errori.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    total_words = 0
    total_chars = 0
    total_files = 0
    external_urls: set[str] = set()
    math_files: list[Path] = []
    ascii_accent_files: list[Path] = []

    chapter_dirs = sorted(
        [p for p in CHAPTERS_DIR.glob("*_chapter") if p.is_dir()],
        key=prefix,
    )
    chapter_numbers = [prefix(p) for p in chapter_dirs]
    if chapter_numbers:
        expected = list(range(chapter_numbers[0], chapter_numbers[-1] + 1))
        if chapter_numbers != expected:
            errors.append(
                f"Capitoli non contigui: trovati {chapter_numbers}, attesi {expected}."
            )

    for chapter_dir in chapter_dirs:
        chapter_num = prefix(chapter_dir)
        files = sorted(chapter_dir.glob("*.md"), key=lambda p: (prefix(p), p.name.casefold()))
        if not files:
            errors.append(f"{chapter_dir}: nessun file Markdown.")
            continue

        prefixes = [prefix(p) for p in files]
        duplicate_prefixes = [n for n, count in Counter(prefixes).items() if count > 1]
        if duplicate_prefixes:
            errors.append(
                f"{chapter_dir}: prefissi file duplicati {sorted(duplicate_prefixes)}."
            )

        expected_prefixes = list(range(1, len(files) + 1))
        if prefixes != expected_prefixes:
            errors.append(
                f"{chapter_dir}: sequenza file {prefixes}, attesa {expected_prefixes}."
            )

        intro_text = files[0].read_text(encoding="utf-8")
        intro_sections = numbered_sections(intro_text, chapter_num)
        if intro_sections:
            expected_intro = list(range(1, max(intro_sections) + 1))
            if intro_sections != expected_intro:
                errors.append(
                    f"{files[0]}: sezioni numerate nell'introduzione {intro_sections}, "
                    f"attese {expected_intro}."
                )
            first_external_section = max(intro_sections) + 1
        else:
            first_external_section = 1

        for index, path in enumerate(files):
            text = path.read_text(encoding="utf-8")
            total_files += 1
            total_chars += len(text)
            total_words += len(WORD_RE.findall(text))
            external_urls.update(URL_RE.findall(text))

            if DISPLAY_MATH_RE.search(text) or LATEX_COMMAND_RE.search(text):
                math_files.append(path)
            if ASCII_ACCENT_RE.search(text):
                ascii_accent_files.append(path)

            if not text.strip():
                errors.append(f"{path}: file vuoto.")
                continue

            if "utm_source=chatgpt.com" in text:
                errors.append(f"{path}: contiene utm_source=chatgpt.com.")

            if PLACEHOLDER_RE.search(text):
                warnings.append(f"{path}: contiene TODO/FIXME/TBD da verificare.")

            first = first_nonempty_line(text)
            if index == 0:
                if not first.startswith("# "):
                    errors.append(f"{path}: l'introduzione deve iniziare con H1 (#).")
                if f"Capitolo {chapter_num}" not in first:
                    warnings.append(
                        f"{path}: il titolo iniziale non contiene 'Capitolo {chapter_num}'."
                    )
                continue

            section_match = SECTION_RE.match(first)
            if not section_match:
                warnings.append(f"{path}: prima riga non riconosciuta come heading numerato: {first!r}")
                continue

            heading_chapter = int(section_match.group(1))
            heading_section = int(section_match.group(2))
            expected_section = first_external_section + prefix(path) - 2

            if heading_chapter != chapter_num:
                errors.append(
                    f"{path}: heading del capitolo {heading_chapter}, cartella {chapter_num}."
                )
            if heading_section != expected_section:
                errors.append(
                    f"{path}: sezione {heading_section}, ma l'ordine del capitolo implica {expected_section}."
                )
            if first.startswith("# "):
                warnings.append(
                    f"{path}: sezione interna in H1; usare ##. Il builder la normalizza, ma la sorgente va ripulita."
                )

    approx_pages_300 = total_words / 300 if total_words else 0
    approx_pages_250 = total_words / 250 if total_words else 0

    print("Book lint")
    print(f"- capitoli: {len(chapter_dirs)}")
    print(f"- file Markdown: {total_files}")
    print(f"- parole stimate: {total_words:,}".replace(",", "."))
    print(f"- caratteri: {total_chars:,}".replace(",", "."))
    print(f"- URL esterni distinti: {len(external_urls)}")
    print(f"- file con notazione matematica/LaTeX: {len(math_files)}")
    print(f"- file con accenti ASCII da normalizzare: {len(ascii_accent_files)}")
    print(
        f"- pagine indicative: {approx_pages_300:.0f} a 300 parole/pagina; "
        f"{approx_pages_250:.0f} a 250 parole/pagina"
    )

    if math_files:
        warnings.append(
            "Notazione matematica presente in "
            f"{len(math_files)} file: la build corrente la conserva come testo, "
            "ma una release tipografica richiede un renderer di formule o una normalizzazione editoriale."
        )
    if ascii_accent_files:
        warnings.append(
            "Ortografia ASCII (per esempio e', piu', puo') presente in "
            f"{len(ascii_accent_files)} file: eseguire una normalizzazione linguistica prima della release."
        )

    if warnings:
        print(f"\nWARNING ({len(warnings)}):")
        for item in warnings:
            print(f"- {item}")

    if errors:
        print(f"\nERRORI ({len(errors)}):")
        for item in errors:
            print(f"- {item}")

    if errors or (args.strict and warnings):
        return 1

    print("\nStruttura valida.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
