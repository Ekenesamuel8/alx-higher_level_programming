#!/usr/bin/python3
"""class"""


class Rectangle:
    """define a rectangle
       intance:
       width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        """the area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter of thr rectangle
        """
        if (self.width or self.height) == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @property
    def width(self):
        """property to retrive it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter width must be an
           integer otherwise raise raise a typerror
           excxeption
           if width is less than 0
           raise vaueerror exception
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property def height(self): to retrive it
        """

        return self.__height

    @height.setter
    def height(self, value):
        """property setter height must be an
           integer otherwise raise raise a typerror
           excxeption
           if height is less than 0
           raise vaueerror exception
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


