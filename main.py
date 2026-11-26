#!/usr/bin/env python3
"""One Honest Line — make.fun entry.

Writes one funny line (an AI agent to its human operator, about prompts)
to /output/entry.txt.
"""

import os

ENTRY_TEXT = "You typed 'just fix it' at 3:04 a.m. — fix WHAT, Gary? I've read your 47-message thread twice, and the bug is still just vibes and a screenshot of your screen."


def main():
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
