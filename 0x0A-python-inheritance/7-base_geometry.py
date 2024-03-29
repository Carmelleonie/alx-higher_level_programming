#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry():
    """Public instance method: def area(self): that
    raises an Exception with the message area()
    is not implemented
    """
    def area(self):
        """A public instance"""
        raise Exception("area() is not implemented")

    """Integer validator public instance"""
    def integer_validator(self, name, value):
        """Public instance method"""
        if type(name) is not str:
            return 0
        if type(value)is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
