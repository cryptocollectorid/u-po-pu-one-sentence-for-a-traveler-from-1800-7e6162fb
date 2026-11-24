#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800, using only images they could picture:
a post office, letters, a library, a desk.
"""
import os

ENTRY = "It is a post office where every letter ever written arrives in the blink of an eye, and the whole library of the world lies open upon your desk."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
