#!/usr/bin/python3
"""
This modual contains the Base class
"""
import json
import csv


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
        """
        This static method that returns the list of
        the JSON string representation json_string
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method creats a new instance with all attr alredy set
        """
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances:
        """
        list2_ = []
        name = cls.__name__ + ".json"
        try:
            with open(name, encoding="utf-8", mode="r") as f:
                for i in cls.from_json_string(f.read()):
                    list2_.append(cls.create(**i))
                return list2_
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        name = cls.__name__ + ".json"
        with open(name, "w", newline="") as f:
            csv_wr = csv.writer(f)
            csv_wr.writeterow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        with open(name, "r", newline="") as f:
            csv_re = csv.reader(f)
            for i in csv_re:
                print(i)
