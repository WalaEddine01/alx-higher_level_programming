#!/usr/bin/python3
"""
This Modual contains the lookup function
"""


def lookup(obj):
    """
    This function returns the list of available attributes and methods of an
    object

    Args:
        obj: it is a object

    Return: returns the list of available attributes and methods of an object
    """
    return dir(obj)
