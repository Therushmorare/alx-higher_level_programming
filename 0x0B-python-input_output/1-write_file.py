#!/usr/bin/python3

""" write function """
def write_file(filename="", text=""):
    """ write encoded file """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
