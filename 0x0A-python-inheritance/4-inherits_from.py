#!/usr/bin/python3
"""
This modual contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    inherits_from function checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: the ibject
        a_class: the class

    Return:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
