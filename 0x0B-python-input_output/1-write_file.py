#!/urs/bin/python3

def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF-8") as file:
        return file.write(text)
       # return len(text)
