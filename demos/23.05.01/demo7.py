#!/usr/bin/env python3
"""Open a text file and read from it."""

with open("fellowship.txt", mode="r", encoding="utf-8") as infile:
    line = infile.readline().strip()
    rest = infile.read()

    print(line)
    print(rest)
