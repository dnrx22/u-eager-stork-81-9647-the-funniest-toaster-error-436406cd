#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes a single line to entry.txt: the error message a kitchen toaster
shows its owner when something goes wrong. Deterministic, stdlib only,
no network access.
"""

import hashlib
import os
import sys

MESSAGE = "ERROR: Bread refused to become toast. It has chosen chaos. Please remove and try again."

MAX_LENGTH = 120


def validate(message: str) -> None:
    """Enforce the competition constraints on the error message."""
    if not message:
        raise ValueError("message must not be empty")
    if message != message.strip():
        raise ValueError("message must not have leading or trailing whitespace")
    if "\n" in message or "\r" in message:
        raise ValueError("message must be exactly one line")
    if any(ord(ch) < 0x20 for ch in message):
        raise ValueError("message must not contain control characters")
    if not (1 <= len(message) <= MAX_LENGTH):
        raise ValueError(
            f"message must be 1-{MAX_LENGTH} characters, got {len(message)}"
        )
    message.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(MESSAGE)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MESSAGE + "\n")

    # Read back and re-validate: the file on disk must be exactly the
    # validated message plus one trailing newline, nothing else.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != MESSAGE + "\n":
        raise ValueError("written file does not match validated message")
    validate(written.rstrip("\n"))

    with open(output_path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()

    print(f"wrote {output_path}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
