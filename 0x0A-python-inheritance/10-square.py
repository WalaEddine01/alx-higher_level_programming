#!/usr/bin/python3
"""
This modual contains the BaseGeometry class
"""
rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    '''
    This is Square class
    '''
    def __init__(self, size):
        rectangle().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This function returns the area of the rectangle
        """
        return self.__size ** 2
