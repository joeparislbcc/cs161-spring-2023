#!/usr/bin/env python3
"""Open a text file for reading and print its contents to screen.

Using a context manager can make managing resources like open files easier and
less error-prone, and is the preferred way to do so.
"""

with open("fellowship.txt", mode="r", encoding="utf-8") as roster:
    for line in roster:
        print(line.strip())

# there's in implicit close() here
