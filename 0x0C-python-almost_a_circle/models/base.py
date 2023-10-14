#!/usr/bin/python3
"""
This modual contains the Base class
"""
import json


class Base:
    """
    This is the Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file hat writes the JSON string representation of
        list_objs to a file
        """
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        name = cls.__name__ + ".json"
        with open(name, encoding="utf-8", mode='w') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
