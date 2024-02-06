#!/usr/bin/python3
"""python iput and output task 0"""


def read_file(filename=""):
    """THIS reads a file text and prints it to stdout
       arg:
       filename: file to bew open
    """

    with open(filename, 'r', encoding="UTF-8") as file:
        plsread = file.read()
        print(plsread)
