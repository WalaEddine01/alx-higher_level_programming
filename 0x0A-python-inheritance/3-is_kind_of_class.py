#!/usr/bin/python3
"""
This modual contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class function check if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class

    Args:
        obj: the object
        a_class: the class

    Return:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
