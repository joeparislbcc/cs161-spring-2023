#!/usr/bin/env python3
"""Open a two text files, one for reading and another for writing."""

# with open("fellowship.txt", mode="r", encoding="utf8") as infile:
#     with open("out.txt", mode="w", encoding="utf8") as outfile:
#         for line in infile:
#             outfile.write(line.upper())

with open("fellowship.txt") as infile, open("out.txt", mode="w") as outfile:
    for line in infile:
        outfile.write(line.upper())
