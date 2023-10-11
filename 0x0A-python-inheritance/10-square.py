#!/usr/bin/python3
"""
This modual contains the BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    This is Square class
    '''
    def __init__(self, size):
        super().__init__(size, size)
        Rectangle(size, size).integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This function returns the area of the rectangle
        """
        return self.__size ** 2
