#!/usr/bin/python3
def print_square(size):
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
