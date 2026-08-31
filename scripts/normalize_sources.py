from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
NUMERIC_H1_RE = re.compile(r"^# (\d+\.\d+\b.*)$")
INLINE_CODE_RE = re.compile(r"(`[^`]*`)")
ASCII_REPLACEMENTS = {
    "e'": "è",
    "piu'": "più",
    "puo'": "può",
    "cosi'": "così",
    "perche'": "perché",
    "gia'": "già",
    "pero'": "però",
    "qualita'": "qualità",
    "attivita'": "attività",
    "realta'": "realtà",
    "probabilita'": "probabilità",
    "modalita'": "modalità",
    "unita'": "unità",
    "societa'": "società",
}
ASCII_ACCENT_RE = re.compile(
    r"(?<!\w)(?:" + "|".join(re.escape(key) for key in ASCII_REPLACEMENTS) + r")(?!\w)",
    re.IGNORECASE,
)


def preserve_case(original: str, replacement: str) -> str:
    if original.isupper():
        return replacement.upper()
    if original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def normalize_prose_segment(segment: str) -> str:
    def repl(match: re.Match[str]) -> str:
        original = match.group(0)
        replacement = ASCII_REPLACEMENTS[original.lower()]
        return preserve_case(original, replacement)

    return ASCII_ACCENT_RE.sub(repl, segment)


def normalize_line(line: str, in_fence: bool) -> str:
    if in_fence:
        return line

    match = NUMERIC_H1_RE.match(line)
    if match:
        line = "## " + match.group(1)

    # Do not touch inline code. The normalizations are ordinary Italian prose
    # fixes and should never rewrite SQL/Python snippets wrapped in backticks.
    parts = INLINE_CODE_RE.split(line)
    for index in range(0, len(parts), 2):
        parts[index] = normalize_prose_segment(parts[index])
    return "".join(parts)


def normalize_text(text: str) -> str:
    output: list[str] = []
    in_fence = False
    fence_marker: str | None = None

    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            output.append(line)
            continue

        output.append(normalize_line(line, in_fence))

    return "".join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalizza convenzioni Markdown e accenti italiani.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Non modifica i file; termina con errore se una normalizzazione sarebbe necessaria.",
    )
    args = parser.parse_args()

    changed: list[Path] = []
    for path in sorted(CHAPTERS_DIR.glob("*_chapter/*.md")):
        original = path.read_text(encoding="utf-8")
        normalized = normalize_text(original)
        if normalized == original:
            continue
        changed.append(path)
        if not args.check:
            path.write_text(normalized, encoding="utf-8")

    if changed:
        action = "Da normalizzare" if args.check else "Normalizzati"
        print(f"{action}: {len(changed)} file")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
        return 1 if args.check else 0

    print("Sorgenti già normalizzate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
