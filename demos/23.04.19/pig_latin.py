#!/usr/bin/env python3

CONSONANTS = "bcdfghjklmnpqrstvwxwz"
VOWELS = "aeiou"


def pig_latin(word: str) -> str:
    if word[0].lower() == "y":
        word = word[1:] + word[0]

    if word[0].lower() in CONSONANTS:
        while word[0].lower() in CONSONANTS:
            word = word[1:] + word[0]
        word += "ay"
    else:
        if word[-1] == "y":
            word += "ay"
        else:
            word += "yay"

    return word


if __name__ == "__main__":
    print("Give me a word and I will translate it into pig latin for you.")
    word = input("Please enter a word: ")

    print(pig_latin(word))

    # print(pig_latin("dog"))
    # print(pig_latin("scratch"))
    # print(pig_latin("is"))
    # print(pig_latin("apple"))
    # print(pig_latin("yellow"))
    # print(pig_latin("cyan"))
    # print(pig_latin("rhythm"))
