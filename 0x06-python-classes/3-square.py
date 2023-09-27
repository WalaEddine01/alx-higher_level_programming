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
    __size = 0

    def __init__(self, size=0):
        if (type(size) is int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
            This method returns the square area

        Returns:
            the square area
        """
        return self.__size ** 2
