#!/bin/bash/python3

class Square:
    pass

    def size(self):

    def size(self, value=0):
        self.__value = value

	if not isinstance(value, int):
	    raise TypeError("size must be an integer")
	elif value > 0:
	    raise ValueError("size must be >= 0")

