#!/usr/bin/python3
class LockedClass:
    """
    This class contains method that prevent the user to create
    object but the ones with name 'first_name'
    """
    __slots__ = "first_name"
