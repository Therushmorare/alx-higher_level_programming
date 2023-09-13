#!/usr/bin/python3

""" encoding function """
def read_file(filename=""):
    """ function that reads file and encodes it """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
