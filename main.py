#!/usr/bin/env python3
"""The Vending Machine Pickup Line — make.fun entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt. Deterministic: the same line every run, no network,
no randomness, stdlib only.

Run:  python3 main.py
"""

import os
import sys

# The line. The angle: the machine malfunctions out of attraction — its
# coils spin before anyone has pressed a button, and it ends up
# dispensing something it was never stocked with. First-person machine
# voice throughout (my coils, I dispense), built only from the machine's
# own world — coils, buttons, dispensing — with the punch landing in the
# last few words, and warm rather than creepy: a crush, not a claim.
ENTRY = (
    "You walked past and my coils spun before you even pressed a "
    "button \u2014 guess I dispense crushes now."
)

# The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR lets the kit
# harness (or a local run) point the output somewhere else.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 200


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the pickup line to ``path`` and return it.

    Enforces the competition gate before writing: 1-200 characters,
    not only whitespace, UTF-8, exactly one line. Fail loudly instead
    of shipping an entry the scorer would refuse.
    """
    if not ENTRY.strip():
        raise SystemExit("refusing to write an empty entry")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in ENTRY:
        raise SystemExit("entry must be exactly one line")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    return ENTRY


def main() -> int:
    entry = write_entry()
    print(f"Wrote {len(entry)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
