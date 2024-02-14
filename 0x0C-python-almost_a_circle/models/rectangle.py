#!/usr/bin/python3
"""rectangle model"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """construtor:
           arg:
           width-width of the rectangle
           height- height of the rectangle
           x- vertical axise of the rectangle
           y- horizontal axise of the rectangle
           id- identity of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """accessing the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """modifying the width
           conditions:
           if value is not int; raise a TypeError with message
           if value is less down or equal to 0;
           raise a ValueError with a message
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """accessing the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """modifying the height
           conditions:
           if value is not int; raise a TypeError with message
           if value is less down or equal to 0;
           raise a ValueError with a message
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """accessing the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """modifying the x axises
           conditions:
           if value is not int; raise a TypeError with message
           if value is less down 0;
           raise a ValueError with a message
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """accessing the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """modifying the y axises
           conditions:
           if value is not int; raise a TypeError with message
           if value is less down 0;
           raise a ValueError with a message
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """displays the rectangle with the string '#'"""
        print("\n" * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x + "#" * self.width)

    def __str__(self):
        """displays a message in a string format"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                "- {self.width}/{self.height}")

    def update(self, *args):
        """assigning arguments to eash of the variables"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
