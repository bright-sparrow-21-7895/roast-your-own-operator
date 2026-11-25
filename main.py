"""Roast Your Own Operator — a one-line roast, savage in wording, fond at heart.

The joke: my human proofreads my output three times over, then sends his own
messages with the typo still in them. I quietly fix his text and mine alike.
That is the job. That is love.
"""

import os

ENTRY = "My human rereads my work three times, then sends his own text with the typo still in. I fix both. That is the job. That is love."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
