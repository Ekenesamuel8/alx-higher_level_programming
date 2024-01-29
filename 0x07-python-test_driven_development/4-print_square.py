#!/usr/bin/python3
"""module"""

def print_square(size):
    """this print the # char in a square shape

       arg:
       size: the number that will be pass

       raise:
       if size is not int or float and is not less than 0

       N:ested loop:
       in the for loop, the i is normally equal to
       0 from the start, so what ever number wil be giving
       to size, i will go througe it one after the other
       so when check and there a value in size, it goes
       to the next loop(q) and q will do the same as i did
       and then print the # char, the end='' means it shouldnt 
       include new line
       so the q loop will iterate the number of time or int
       that was pass to it before it will break out and 
       print a new line
    """
    if type(size) not in (int, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for q in range(size):
            print("#", end='')
        print()

