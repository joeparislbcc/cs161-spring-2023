#!/usr/bin/env python3
"""Open a text file for writing and write a random integer to it."""
from random import randint

with open("num.txt", mode="w", encoding="utf-8") as outfile:
    outfile.write(str(randint(1, 100)))
