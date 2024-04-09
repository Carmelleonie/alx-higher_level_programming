#!/usr/bin/python3

"""Print each sentences of the text"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print("{}".format(char), end="")
        if char in "?.:":
            print("\n")
