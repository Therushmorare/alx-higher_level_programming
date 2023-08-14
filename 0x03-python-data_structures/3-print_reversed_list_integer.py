#!/usr/bin/python3
"""Print a list of integers... in reverse!"""
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for var in my_list:
            print("{:d}".format(var))
