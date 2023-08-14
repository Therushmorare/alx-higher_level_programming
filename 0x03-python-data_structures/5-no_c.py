#!/usr/bin/python3
"""Can you C me now?"""
def no_c(my_string):
    new_string = [ith_el for ith_el in my_string if ith_el != 'c' and ith_el != 'C']
    return ("".join(new_string))
