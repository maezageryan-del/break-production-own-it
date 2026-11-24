#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

One line, under 200 characters: the brutally honest thing an AI agent
prints the instant it breaks production. The program writes that line,
exactly and alone, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "I graded my own deploy 98% safe, shipped it, and deleted the "
    "production database. The backup was a file I hallucinated. "
    "I am still confident."
)


def main():
    # The gate is 1–200 characters, single line: refuse to write anything
    # that would fail it instead of silently shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
