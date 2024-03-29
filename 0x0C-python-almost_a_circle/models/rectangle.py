#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

    """width, height, x, y must be an integer
            if not raise TypeError"""
    """get and set the the parameter of the class using getter and setter"""

    # a getter function to get the width
    @property
    def width(self):
        return self.__width
        #a setter function
    @width.setter
    def width(self, width):
        if width is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


    @property
        #set the height
    def height(self):
        return self.__height
        #setter function to set the value of the height
    @height.setter
    def height(self, height):
        if height is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x


    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if y is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y


    def area(self):
        """to determine the area of the rectangle"""
        return self.__width * self.__height


    def display(self):
        for i in range(self.width):
            for j in range(self.height):
                print("#", end="")
            print()


    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        lst = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in lst:
                    setattr(self, key, value)



    def to_dictionary(self):
        """Returns the dict representation of a Rectangle"""

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.__width
        dictionary['height'] = self.__height
        dictionary['x'] = self.__x
        dictionary['y'] = self.__y
        return dictionary
