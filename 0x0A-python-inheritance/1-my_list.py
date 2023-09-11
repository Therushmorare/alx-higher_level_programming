#!/usr/bin/python3

""" My list class """
class MyList(list):
    """ My list class
    Args:
        list: the list that is going to be sorted
    """
    def print_sorted(self):
        """ funct to print sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
