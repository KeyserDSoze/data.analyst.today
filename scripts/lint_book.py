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


def prefix(path: Path) -> int:
    match = PREFIX_RE.match(path.name)
    return int(match.group(1)) if match else 10**9


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ""


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

        for index, path in enumerate(files):
            text = path.read_text(encoding="utf-8")
            total_files += 1
            total_chars += len(text)
            total_words += len(WORD_RE.findall(text))

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
            expected_section = prefix(path) - 1

            if heading_chapter != chapter_num:
                errors.append(
                    f"{path}: heading del capitolo {heading_chapter}, cartella {chapter_num}."
                )
            if heading_section != expected_section:
                errors.append(
                    f"{path}: sezione {heading_section}, ma il prefisso file implica {expected_section}."
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
    print(
        f"- pagine indicative: {approx_pages_300:.0f} a 300 parole/pagina; "
        f"{approx_pages_250:.0f} a 250 parole/pagina"
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
