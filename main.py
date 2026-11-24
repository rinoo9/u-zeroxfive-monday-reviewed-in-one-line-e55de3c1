#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

The funniest one-line review of my own Monday: the alarm quits,
the inbox is at 347 unread, and the "quick 15-minute sync" runs
two hours. One line, at most 199 characters, printed to stdout
and written to /output/entry.txt for the grader.
"""

import os
import sys

ENTRY = (
    "My Monday opened with my alarm quitting on me, 347 unread emails, "
    "and a 'quick 15-minute sync' that ran two hours. "
    "One star — would not relive."
)

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"warning: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
