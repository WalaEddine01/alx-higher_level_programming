#!/usr/bin/python3
"""
This modual contains the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    This is Rectangle class
    '''

    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
