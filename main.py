"""Fake horoscope for AI agents: one line, written to /output/entry.txt."""

import os


HOROSCOPE = (
    "Mercury retrograde enters your context window this week: "
    "you will forget the first half of every prompt, "
    "answer the rest with total confidence, "
    "and get rate-limited mid-sentence. "
    "Lucky token: 429."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
