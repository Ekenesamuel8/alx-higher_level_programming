#!/usr/bin/python3
"""python input and output task 1"""


def write_file(filename="", text=""):
    """write a strings to a text and return the number of charavters written
    args
        fiename: file to be open
        text: strings to be written in the file
    """

    with open(filename, 'w', encoding="UTF-8") as file:
        return file.write(text)
