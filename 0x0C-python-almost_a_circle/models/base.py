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
        save_to_file that writes the JSON string representation of
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
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This method  writes the CSV string representation of
        list_objs to a file
        """
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as f:
            pass

    @classmethod
    def load_from_file_csv(cls):
        """
        class method that returns a list of instances
        """
        from models.rectangle import Rectangle
        from models.square import Square

        list2_ = []
        name = cls.__name__ + ".csv"
        with open(name, encoding="utf-8", mode="r") as f:
            reader = csv.DictReader(f)
            for i in reader:
                ins = cls.create(**i)
                list2_.append(ins)
            return list2_

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        This is draw method
        """
        import turtle

        turtle.bgcolor("black")
        a = list_rectangles + list_squares
        for i in a:
            tu = turtle.Turtle()
            tu.forward(i.width)
            tu.left(90)
            tu.forward(i.height)
            tu.left(90)
            tu.forward(i.width)
            tu.forward(i.height)
            tu.left(90)
            tu.end_fill()
        turtle.done()
