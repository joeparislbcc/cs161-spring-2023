#!/usr/bin/env python3
"""Find a word that contains the vowels 'a', 'e', 'i', 'o', and 'u' in order.

The provided dictionary.txt file contains 234,936 English words in alphabetical
order, one word per line. Using this file as input, write a Python program that
will:

1. Open the file.
2. Read in each word one at a time.
3. Normalize the word.
4. Extract the vowels from the word.
5. Test to see if all the vowels appeared in order.
"""
import sys

VOWELS = "aeiou"


def normalize_word(word: str) -> str:
    """Convert to all lowercase and strip any leading or trailing whitespace."""
    return word.lower().strip()


def main():
    try:
        filename = input("Please enter the name of the file to read from: ")
    except EOFError:
        sys.exit(-1)

    try:
        with open(filename, mode="r", encoding="utf-8") as infile:
            for word in infile:
                clean_word = normalize_word(word)

                # extract the vowels
                vowels_in_word = ""
                for character in clean_word:
                    if character in VOWELS:
                        vowels_in_word += character

                if vowels_in_word == VOWELS:
                    print(clean_word)
    except FileNotFoundError:
        print(f"File not found: {filename}.")
        sys.exit(-2)


if __name__ == "__main__":
    main()

    sys.exit(0)
