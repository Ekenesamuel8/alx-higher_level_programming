#!/usr/bin/python3
"""Defines class Rectangle"""

class Rectangle:
    """Instantiation with optional
        arg:
        width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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
        return self.__height

    @height.setter
    def height(self, value):
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

