#!/usr/bin/python3
from models/rectangle import Rectangle
class Square(Rectangle):
	super().__init__(size, size, x, y)
	self.__width = size
	self.__height = size
	self.__x = x
	self.__y = y
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)


    @property
    #get the value of the size
    def size(self):
        return self.__width
    @size.setter
    def size(self, size):
        if width is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = size


    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        lst = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in names:
                    setattr(self, key, value)



    def to_dictionary(self):
        new ={}
        new['id'] = self.__id
        new['size'] = self.__width
        new['x'] = self.__x
        new['y'] = self.__y
        return new
            
