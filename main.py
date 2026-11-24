#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one deadpan line — a robot vacuum's excuse for missing a spot —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only.
"""

import os

LINE = "My sensors report the crumbs have unionized. One crumb is dirt; a hundred is a picket line, and I do not cross picket lines."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the graded file must be exactly the line,
    # byte for byte — a short or padded write would score as a different entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(f"entry.txt mismatch: wrote {len(written)} chars, expected {len(LINE)}")


if __name__ == "__main__":
    main()
