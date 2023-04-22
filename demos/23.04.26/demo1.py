#!/usr/bin/env python3
"""Open a text file for writing and print its contents to screen."""

# open the file explicitly setting its mode and encoding
roster = open("fellowship.txt", mode="w", encoding="utf-8")

for line in roster:
    print(line)

roster.close()  # be sure to close your files when you are done with them!

# This will not work as written. Note the directory we are in when the program
# is run. This can be fixed by creating a launch.json file and adding
# "cwd": "${fileDirname}" to set the current working directory.
