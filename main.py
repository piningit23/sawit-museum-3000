#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun program/v1 entry.

Writes one museum label to /output/entry.txt: the label a museum in the
year 3000 puts beside an ordinary object from today — a stapler, read by
curators who have never seen one in use and have concluded, quite
confidently, that humans pinned dead trees together so the trees could
not leave.

Deterministic, stdlib-only, no network, no clock, no randomness, no file
reads. The label is a fixed string: one line, in English, original.
"""

import os

ENTRY = (
    "Stapler, c. 2025. Ritual binding device. "
    "Humans pinned dead trees together so the trees could not leave."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding space")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
