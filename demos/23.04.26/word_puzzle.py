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


def sanitize_word(word: str) -> str:
    return word.strip().lower()


def get_vowels(word: str) -> str:
    VOWELS = "aeiou"

    vowels_in_word = ""
    for letter in word:
        if letter in VOWELS:
            vowels_in_word += letter

    return vowels_in_word


def main():
    VOWELS_IN_ORDER = "aeiou"
    index = 1

    with open("dictionary.txt", mode="r", encoding="utf-8") as source:
        for word in source:
            if len(word) >= len(VOWELS_IN_ORDER):  # optimization
                clean_word = sanitize_word(word)
                vowels_in_word = get_vowels(clean_word)
                if vowels_in_word == VOWELS_IN_ORDER:
                    print(f"{index:>3}. {clean_word}")
                    index += 1


if __name__ == "__main__":
    main()
