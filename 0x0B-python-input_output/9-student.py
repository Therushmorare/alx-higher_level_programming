#!/usr/bin/python3

""" class student """
class Student:
    """Student obj"""
    def __init__(self, first_name, last_name, age):
        """ initialize class
            Args:
                first_name (string): student first name
                last_name (string): student last name
                age (int) student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return json string """
        return self.__dict__
