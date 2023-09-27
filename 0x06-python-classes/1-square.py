#!/usr/bin/python3
"""
This moduale defines a class for working with square
"""


class Square:
    """
    This class defines a Square

    Attributes:
        __size: the length of the side of the square
    """
    __size = None

    def __init__(self, size):
        self.__size = size
