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

    def to_json(self):
        """
        to_json function returns a dictionary of a student instance
        """
        return {"first_name": self.first_name, "last_name": self.last_name,
                "age": self.age}
