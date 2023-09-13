#!/usr/bin/python3

""" import modules """
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" adds all arguments to a Python list, and then save them to a file"""
json_filename = "add_item.json"

if os.path.exists(json_filename):
    my_list = load_from_json_file(json_filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, json_filename)

