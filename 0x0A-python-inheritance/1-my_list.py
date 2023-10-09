#!/usr/bin/python3
"""
This Modual contains the lookup class with its properties
"""


class MyList(list):
    """
    This is MyList class that that inherits from list
    """
    def __init__(self):
        """
        this is the consteructore of MyList class
        """
        super().__init__(self)

    def print_sorted(self):
        """
        This is print_sorted method of a class
        that prints the list, but sorted (ascending sort)
        """
        a = self.copy()
        a.sort()
        print(a)
