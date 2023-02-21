#!/usr/bin/python3


"""An empty class in Square"""


class Square():
    """Square, an empty class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
