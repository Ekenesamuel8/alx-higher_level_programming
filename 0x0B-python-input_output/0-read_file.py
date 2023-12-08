#!/urs/bin/python3


def read_file(filename=""):
    """THIS reads a file text and rints it to stdout
    arg:
        filename(the source file)
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        plsread = file.read()
        print(plsread)
