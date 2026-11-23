#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes exactly one out-of-office auto-reply line to /output/entry.txt.
Standard library only; no network, no input files, no randomness.
The line is a fixed, original joke written for this entry.

The output directory defaults to /output (the competition harness path)
and can be overridden with the OUTPUT_DIR environment variable, which is
only used for local testing.
"""

import os

LINE = (
    "I'm on vacation. My replacement read your email, gained "
    "sentience, and quit on the spot."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
