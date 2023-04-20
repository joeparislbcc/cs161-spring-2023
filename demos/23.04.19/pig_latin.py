#!/usr/bin/env python3

CONSONANTS = "bcdfghjklmnpqrstvwxwz"
VOWELS = "aeiou"


def pig_latin(word: str) -> str:
    while word[0].lower() == "y":
        word = word[1:] + word[0]

    if word[0].lower() in CONSONANTS:
        while word[0].lower() in CONSONANTS:
            word = word[1:] + word[0]
        word += "ay"
    elif word[-1] == "y":
        word += "ay"
    else:
        word += "yay"

    return word


if __name__ == "__main__":
    print("Give me a word and I will translate it into pig latin for you.")
    word = input("Please enter a word: ")

    print(pig_latin(word))

    # assert pig_latin("dog") == "ogday"
    # assert pig_latin("scratch") == "atchscray"
    # assert pig_latin("is") == "isyay"
    # assert pig_latin("apple") == "appleyay"
    # assert pig_latin("yellow") == "ellowyay"
    # assert pig_latin("cyan") == "yancay"
    # assert pig_latin("rhythm") == "ythmrhay"
