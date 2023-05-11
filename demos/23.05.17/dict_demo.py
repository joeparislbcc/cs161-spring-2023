#!/usr/bin/env python3
"""Count the words in the provided text file."""
import string
from operator import itemgetter
from pathlib import Path
from pprint import pprint


def add_word(word: str, word_counts: dict[str, int]) -> None:
    """Update word_counts, adding new word if necessary."""
    word_counts[word] = word_counts.get(word, 0) + 1


def sanitize_word(word: str, trans_table: dict[int, int | None]) -> str:
    """Sanitize word.

    Convert word to lowercase stripping any punctuation and leading/trailing
    whitespace."""
    return word.translate(trans_table)


def main():
    filepath = Path("dracula.txt")

    word_counts: dict[str, int] = {}

    trans = str.maketrans(
        string.ascii_uppercase, string.ascii_lowercase, string.punctuation + "“" + "”" + "’"
    )

    with open(filepath, mode="r", encoding="utf8") as infile:
        text = infile.readlines()

    for line in text:
        words = line.strip().split()

        for word in words:
            add_word(sanitize_word(word, trans), word_counts)

    most_common = sorted(word_counts.items(), key=itemgetter(1))
    pprint(most_common[-10:])


if __name__ == "__main__":
    main()
