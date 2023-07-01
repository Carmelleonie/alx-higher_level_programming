#!/usr/bin/python3
"""A class Student that defines a student

"""

class Student():
    """Definition fo the class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(element) == str for element in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

        return self.__dict__
