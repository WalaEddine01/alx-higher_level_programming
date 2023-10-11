#!/usr/bin/python3
"""
This modual contains the calss_tojson function
"""


def class_to_json(obj):
    """
    this functionconverts a class data to json obj

    Args:
        obj: the class obj
    """
    return obj.__dict__
