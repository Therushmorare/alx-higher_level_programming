#!/usr/bin/python3

""" json moduule """
import json

""" function load from """
def load_from_json_file(filename):
    """ loads file via json """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
