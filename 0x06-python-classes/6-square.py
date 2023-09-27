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
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        if (len(position) != 2):
            raise IndexError("Index out of the range")
        if (type(size) is int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (type(position) is not tuple or type(position[0]) is not int
                or type(position[1]) is not int or len(position) != 2
                or position[1] < 0 or position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        a = self.__position[1]
        if j == 0:
            print()
            return
        while a > 0:
            print()
            a = a - 1
        for i in range(0, j):
            for k in range(0, j + self.__position[0]):
                if k >= self.__position[0]:
                    print("#", end="")
                else:
                    print(' ', end="")
            print()

    @property
    def position(self):
        """
        getter of position

        Returns:
            tuple: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter of position

        Args:
            value (tuple): position
        """
        if (type(value) is not tuple or type(value[0]) is not int
                or type(value[1]) is not int or len(value) != 2
                or value[1] < 0 or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
