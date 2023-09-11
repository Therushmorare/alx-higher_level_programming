#!/usr/bin/python3

""" My list class
    Args:
        list: the list that is going to be sorted
"""
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

