#!/usr/bin/python3
"""module"""


def add_integer(a, b=98):
    """
    Adds two integer

    Parameters:
    a (int or float) will be pass
    b (int 0r float) will be pass

    Returns:
    int: addition of two numbers

    Raise:
    TypeError: if a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

    #   if __name__=="__main__":
    #      import doctest
    #     doctest.testfile("tests/0-add_integer.txt")
