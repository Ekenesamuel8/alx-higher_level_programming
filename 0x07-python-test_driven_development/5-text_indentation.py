#!/usr/bin/python3
"""print text"""


def text_indentation(text):
    """print text with two argument and new line
       arg:
       text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """token = text.split('?', ':')
    return(token)
    """
    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
