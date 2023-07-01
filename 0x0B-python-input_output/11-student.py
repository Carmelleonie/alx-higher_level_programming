#!/usr/bin/python3
"""A class Student that defines a student

"""

class Student():
    """Updating class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name =  last_name
        self.age =  age

    def to_json(self, attrs=None):
        if (type(attrs) is list and all(type(element) for element in attrs)):
            return {key:getattr(self, key) for key in attrs if hasattr(self,key)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
