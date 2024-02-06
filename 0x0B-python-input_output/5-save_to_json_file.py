"""pythjon input and output task 5"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file, using
       a JSON representation
    args:
        my_obj: the object to be written in the textfile
         filename: the text file
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
					    ~
    /bin/bash: /urs/bin/python3: No such file or directory
