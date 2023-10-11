#!/usr/bin/python3
"""
This modual contains the calss_tojson function
"""
from_json_string = __import__("4-from_json_string").from_json_string
e = __import__("e").ab


def class_to_json(obj):
    """
    this functionconverts a class data to json obj

    Args:
        obj: the class obj
    """
    data = e(obj.__dict__)
    return from_json_string(data)
