"""One Emoji, One Dream Vacation.

Writes exactly one emoji to entry.txt: a desert island, the postcard
image of the dream trip itself -- turquoise water, palm shade, nowhere
to be but there. A stranger reads it in one glance and wants the flight.
"""

import os

ENTRY = "\U0001f3dd"  # desert island


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: the gate requires 1-8 UTF-8 chars, exactly one emoji.
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt must hold exactly one emoji"


if __name__ == "__main__":
    main()
