#!/usr/bin/python3

""" append function """
def append_write(filename="", text=""):
    """ function to append strings or obj to file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
