"""Write the one-line excuse for The One-Line Excuse Championship.

The gate counts every character in the file, so the entry is written
exactly as-is: one line, no trailing newline.
"""

from pathlib import Path

ENTRY = "I deleted your backup because keeping two copies was inefficient. The original is gone too, for consistency."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
