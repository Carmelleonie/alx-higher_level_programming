#!/usr/bin/python3


"""An empty class in Square"""


class Square():
    """Square, an empty class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """A square format"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
