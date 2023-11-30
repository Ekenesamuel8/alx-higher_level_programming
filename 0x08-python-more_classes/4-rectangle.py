#!/usr/bin/python3
"""defines class Rectangle"""


class Rectangle:
    """Class that defines properties of square

         Attributes:
         size: size of a square (1 side).
    """

    def __init__(self, width=0, height=0):
        """Instantiation with optional
        arg:
            width and height
        """

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

    def area(self):
        """calculate the area of the rectangle
           width * height
        """

        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter of the rectangle
           2 * (width + height)
        """

        if (self.width or self.height) == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def _draw_rectangle(self):
        """obtains a strings representation of a object
        """

        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instances.

           Return:
           The output of _draw_rectangle, which creates a string
           representation of the rectangle suitable for printing.

        """

        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

            Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
