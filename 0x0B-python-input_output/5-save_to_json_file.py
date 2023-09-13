#!/usr/bin/python3

""" json module """
import json

""" function save to json """
def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

