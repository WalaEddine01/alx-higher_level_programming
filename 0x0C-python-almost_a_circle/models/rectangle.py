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
        """
        This is the initialize function
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width > 0:
            self.__width = width
        else:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height > 0:
            self.__height = height
        else:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x >= 0:
            self.__x = x
        else:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y >= 0:
            self.__y = y
        else:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """
        This is the getter function for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        This is the setter function for width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width > 0:
            self.__width = width
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """
        This is the getter function for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        This is the setter function for height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height > 0:
            self.__height = height
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """
        This is the getter function for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        This is the setter function for x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x >= 0:
            self.__x = x
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """
        This is the getter function for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        This is the setter function for y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y >= 0:
            self.__y = y
        else:
            raise ValueError("y must be >= 0")
