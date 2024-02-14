#!/usr/bin/python3


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, heigth=size)
        
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
	                                        self.id, self.__x, self.__y,
                                                self.__width, self.__height)
