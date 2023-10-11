#!/usr/bin/python3
"""
This modual contains a Student class
"""


class Student:
    """
    this is student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict_ = {}
        """
        to_json function returns a dictionary of a student instance
        """
        if attrs is None:
            return {"age": self.age, "last_name": self.last_name,
                    "first_name": self.first_name}
        else:
            for i in attrs:
                if hasattr(self, i):
                    dict_[i] = getattr(self, i)
        return dict_

    def reload_from_json(self, json):
        '''
        reload_from_json function that repalce all
        attributes of the Student
        '''
        for key, value in json.items():
            setattr(self, key, value)
