#!/urs/bin/python3

def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        eappend = file.write(text)
        return (eappend)
