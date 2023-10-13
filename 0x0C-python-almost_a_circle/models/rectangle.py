#!/usr/bin/python3
"""
This modual is contains the Rectangle class
That inhirits from the Base class
"""
from models.base import Base


class Rectangle(Base):
    '''
    This is Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
