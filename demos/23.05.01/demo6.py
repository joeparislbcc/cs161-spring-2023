#!/usr/bin/env python3
"""Read a particular line from a text file.

Both the name of the text file and the number of the line to read from it are
specified by the user."""
import sys


def main():  # McCabe strikes again!!
    while True:
        try:
            filename = input("Please enter the name of the file to read from: ")
        except EOFError:
            sys.exit()
        except KeyboardInterrupt:
            print("Goodbye!")
            sys.exit()

        try:
            with open(filename, mode="r", encoding="utf=8") as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"{filename}: File not found")
        else:
            break

    while True:
        try:
            target_line_number = int(input("Please enter the line number to read: "))
        except ValueError:
            print("Invalid line number. Please try again.")
        else:
            break

    try:
        print(f'Line {target_line_number} is "{lines[target_line_number - 1]}"')
    except IndexError:
        print(f"Line {target_line_number} does not exist in file {filename}")


if __name__ == "__main__":
    main()
