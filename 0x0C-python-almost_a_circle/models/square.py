#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, width, height, x, y):
        super().__init__(size, size, x, y)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if width is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
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


    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        lst = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in lst:
                    setattr(self, k, v)



    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
