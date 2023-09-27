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

    @property
    def size(self):
        """
        get the size of the Square

        Return:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of the square

        Args:
            value (int): the new size of the square

        Raises:
        TypeError: if the value is not an int
        ValueError: if the value is less than 0
        """
        if (type(value) is int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        print in stdout the square with the character #

        Return: Nothing
        """
        j = self.__size
        if j:
            for i in range(0, j):
                for k in range(0, j):
                    print("#", end="")
                print()
        else:
            print()
