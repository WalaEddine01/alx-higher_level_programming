#!/usr/bin/python3
"""
This modual contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    This function check if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class

    Args:
        obj: the object
        a_class: the class

    Return:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
