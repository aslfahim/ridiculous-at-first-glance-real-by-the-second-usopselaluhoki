#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea:
professional excuse writers for overworked employees.
Standard library only.
"""

import os

SENTENCE = (
    "We sell bulletproof sick-day and deadline excuses, ghostwritten by ex-HR managers, "
    "to overworked employees \u2014 because one airtight alibi can save your job, "
    "your promotion, and your whole weekend."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
