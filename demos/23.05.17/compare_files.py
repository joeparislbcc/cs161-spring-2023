#!/usr/bin/env python3
"""Count the words in the provided text file."""
import string
from pathlib import Path


def sanitize_line(line: str) -> list[str]:
    trans = str.maketrans(
        string.ascii_uppercase + "’",
        string.ascii_lowercase + "'",
        '“”!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~',
    )

    return [
        word.strip(string.punctuation + string.whitespace).translate(trans) for word in line.split()
    ]


def get_words_in_file(filename: str, stop_words: list[str]) -> list[str]:
    with open(Path(filename), mode="r", encoding="utf8") as infile:
        text = infile.readlines()

    all_words: list[str] = []

    for line in text:
        words = sanitize_line(line)
        for word in words:
            if word not in stop_words:
                all_words.append(word)

    return all_words


def main():
    with open(Path("stop-words.txt"), mode="r", encoding="utf8") as infile:
        stop_words = [word.strip() for word in infile]

    dracula_text = set(get_words_in_file("dracula.txt", stop_words))
    frankenstein_text = set(get_words_in_file("frankenstein.txt", stop_words))

    common_words = dracula_text & frankenstein_text

    print(f'The novels "Dracula" and "Frankenstein" have {len(common_words):,} words in common.')
    print(f'"Dracula" has {len(dracula_text - frankenstein_text):,} words unique to it.')
    print(f'"Frankenstein" has {len(frankenstein_text - dracula_text):,} words unique to it.')


if __name__ == "__main__":
    main()
