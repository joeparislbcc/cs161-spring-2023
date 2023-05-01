#!/usr/bin/env python3
"""Read a particular line from a text file.

Both the name of the text file and the number of the line to read from it are
specified by the user."""


def main():
    filename = input("Please enter the name of the file to read from: ")
    target_line_number = input("Please enter the line number to read: ")

    try:
        with open(filename, mode="r", encoding="utf-8") as infile:
            target_line_number = int(target_line_number)
            line_count = 1

            for line in infile:
                if line_count == target_line_number:
                    print(f'Line {target_line_number} of file {filename} is "{line}"')
                    break
                line_count += 1
            else:  # for...else
                print(f"Line {target_line_number} of file {filename} does not exist")

    except FileNotFoundError:
        print(f"The file {filename} does not exist")

    except ValueError:
        print(f"{target_line_number} is not a legal line number")


if __name__ == "__main__":
    main()
