#!/usr/bin/python3
"""module"""

def say_my_name(first_name, last_name=""):
    """prints the name that was passed
      arg:
      first_name = first name
      last_name = second name

      return:
      my name is <first name> <second name>

      raise:
      if first_name or last_name is not a string
    """

    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance (last_name, str):
        raise TypeError("last_name must be a string")
    else:
    	print(f"My name is {first_name} {last_name}")


