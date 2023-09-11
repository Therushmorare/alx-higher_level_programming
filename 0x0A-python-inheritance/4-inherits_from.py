#!/usr/bin/python3

""" check if object is subclass """
def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class

