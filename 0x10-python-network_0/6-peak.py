#!/usr/bin/python3
"""
This module contains method that filds a peak in list
"""


def find_peak(list_of_integers):
    """
    this is the find_peak method finds a peak in a list
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
