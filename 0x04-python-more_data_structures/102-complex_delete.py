#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_elements = list(a_dictionary.keys())

    for i in list_elements:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
