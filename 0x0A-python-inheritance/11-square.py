#!/usr/bin/python3
"""
This modual contains the Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    This is Square class
    '''
    def __init__(self, size):
        Rectangle(size, size).integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This function returns the area of the rectangle
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
