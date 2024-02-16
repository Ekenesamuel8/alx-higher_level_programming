#!/usr/bin/python3
"""square model"""
from models.rectangle import Rectangle
"""import from rectanghle model"""


class Square(Rectangle):
    """inherite from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructors"""
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    @property
    def size(self):
        """access the size attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """update the size attribute"""

        self.width = value
        self.height = value

    def __str__(self):
        """display inthis format"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
                f"- {self.size}")

    def update(self, *args, **kwargs):
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            print()

    def to_dictionary(self):
        """Returns a dict representation
        """

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
