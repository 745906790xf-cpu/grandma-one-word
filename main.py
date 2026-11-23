"""One Word From Grandma entry for make.fun.

Writes one word to /output/entry.txt: the single word a grandma would
text about AI. The sandbox runs this program twice and both runs must
write the same bytes, so the word is a fixed string with no randomness,
clock, or network access.
"""

import os

WORD = "Beepboop"


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the word as UTF-8 with no trailing newline.

    Keeping the bytes exact matters: the gate accepts 1 to 30 characters
    of UTF-8 text, and the two sandbox runs must produce identical
    output.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
