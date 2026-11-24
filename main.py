"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt (1-160 characters).

The label: every human alive has told someone they are "five minutes
away" while still on the sofa. The joke is recognition, the turn lands
in the last few words ("for the next forty minutes"), and it reads like
a real printed warning ("WARNING: ... Plan accordingly.").

The gate accepts only UTF-8 text of 1 to 160 characters, not only
white space, so this program refuses to write anything outside that
range instead of silently shipping an invalid entry.
"""

import os

LABEL = (
    "WARNING: This human will say \"I'm five minutes away\" "
    "for the next forty minutes. Plan accordingly."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def build_label() -> str:
    """Return the label as exactly one line, with no stray whitespace."""
    line = " ".join(LABEL.split())
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"label is {len(line)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    return line


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(build_label() + "\n")


if __name__ == "__main__":
    main()
