#!/usr/bin/python3
"""defines class Rectangle"""

class Rectangle:
    """Instantiation with optional
        arg:
        width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.width or self.height) == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @property
    def width(self):
        """property def width(self): to retrieve it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter def width(self, value)
            width must be an integer
            otherwise raise a TypeError exception
            if width is less than 0,
	    raise a ValueError exception
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property def width(self): to retrieve it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter def width(self, value)
            width must be an integer
            otherwise raise a TypeError exception
            if width is less than 0,
	    raise a ValueError exception
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
