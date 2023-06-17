#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout:
"""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")

if __name__ == "__main__":
    main()
