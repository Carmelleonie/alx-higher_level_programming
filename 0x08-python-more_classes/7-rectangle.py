#!/usr/bin/python3


"""
More advanced features about OOp in python
"""


class Rectangle:
    """Rectangle class and its mathematic properties"""


    """Public class attribute"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__width
    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """This is the area of the rectangle"""
    def area(self):
        return self.__width * self.__height

    """This is the perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    """A design of the rectangle"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += Rectangle.print_symbol * self.width
            if i != self.height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
