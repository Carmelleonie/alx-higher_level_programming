#!/usr/bin/python3
"""Rectangle inherited from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """A public instance"""
        return self.__width * self.__height

    def __str__(self):
        """str() function"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
