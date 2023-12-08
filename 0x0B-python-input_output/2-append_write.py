#!/usr/bin/python3
"""python input/output task 2"""


def append_write(filename="", text=""):
    """append a string at the end of a textfile and return the number of character added
    args
        filename: text file to be open
        text: string to be append
    """

    with open(filename, 'a') as file:
        file.write(text)
        return len(text)
