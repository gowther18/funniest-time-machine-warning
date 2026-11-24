"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The label is a deadpan safety notice: the emergency-exit instruction
is perfectly official — until the last word strands the reader in 1987.
"""
import os

TEXT = "WARNING: In case of emergency, exits are located in 1987."


def validate(text):
    """Gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1 to 120 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(TEXT))


if __name__ == "__main__":
    main()
