#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — winning duel entry (D6).

Writes the two-line explanation to /output/entry.txt.
Line 1: a traffic jam explained to a 10-year-old through the analogy of
ants carrying crumbs through a straw. Line 2: why the analogy works —
what it maps and what it leaves out.
"""

import os

ENTRY = (
    "A traffic jam is a line of ants carrying crumbs through a straw, "
    "each one waiting for the ant ahead to move before it can take a step.\n"
    "The ants explain the single-file crawl and why one slow ant holds "
    "everyone up, but they leave out that drivers can change lanes, honk, "
    "and choose a different road, while ants never overtake or pick another straw.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
