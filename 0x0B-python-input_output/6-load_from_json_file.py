#!/usr/bin/python3
"""task 6 of python input output"""
import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"
    arg:
        filename: the file
    """

    with open(filename) as file:
        return json.load(file)
