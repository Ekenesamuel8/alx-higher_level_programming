#!/usr/bin/python3
"""python input and output task 4"""
import json


def from_json_string(my_str):
    """returns an object representatiom by json sting
        arg
       my_str: the string
    """

    return json.loads(my_str)
