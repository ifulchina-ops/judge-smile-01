#!/usr/bin/env python3
"""Make the Judge Smile — make.fun bounty entry.

Writes one line (<=200 chars) about a small good thing that happened today
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local dry runs).

The line: a stray cat that always steals my fried chicken finally paid
rent — with a dead lizard on the doorstep. Warmth, surprise, one concrete
detail, fresh words: exactly what the judge's brief asks for.
"""

import os
import sys


LINE = (
    "At dawn the stray cat that always steals my fried chicken left a "
    "dead lizard on my doorstep \u2014 rent, at last, paid in full."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    # Gate (competition.yaml): UTF-8 text of 1-200 chars, not only whitespace.
    if not text or not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of gate (1-200, non-blank)",
              file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
