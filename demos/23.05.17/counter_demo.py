#!/usr/bin/env python3
"""Count the words in the provided text file."""
import string
from collections import Counter  # https://realpython.com/python-counter/
from pathlib import Path
from pprint import pprint


def main():
    filepath = Path("dracula.txt")

    trans = str.maketrans(
        string.ascii_uppercase, string.ascii_lowercase, string.punctuation + "“" + "”" + "’"
    )

    with open(filepath, mode="r", encoding="utf8") as infile:
        text = infile.read().strip()

    text = text.translate(trans)

    word_counts = Counter(text.strip().split())
    pprint(word_counts.most_common(10))

    letter_counts = Counter(text.strip())
    pprint(letter_counts)


if __name__ == "__main__":
    main()
