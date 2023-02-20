#!/usr/bin/python3


"""
This function is about an empty class Rectangle that defines a rectangle
"""


class Rectangle():
    """Defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """The area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    """The rectangle format"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += "#" * self.width
            if i != self.height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'


    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
