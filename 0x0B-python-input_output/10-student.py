#!/usr/bin/python3

""" class student """
class Student:
    """Student obj """

    def __init__(self, first_name, last_name, age):
        """ initialize class
            Args:
                first_name (string): student name
                last_name (string): student surname
                age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ save the values in dic """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
           if key in attrs:
                new_dictionary[key] = value
        return new_dictionary
