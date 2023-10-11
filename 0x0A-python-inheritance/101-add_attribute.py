#!/usr/bin/python3
"""
This modual contains add_attribute function
"""


def add_attribute(obj, key, value):
    """
    add_attribute function that adds a new att to an obj
    if it possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("cant add new attribute")
    setattr(obj, key, value)
