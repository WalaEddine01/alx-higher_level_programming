#!/usr/bin/python3
"""
This Modual for Rectangle class and Its operation
"""


class Rectangle:
    """
    This class represents a sRectangle

    Attributes:
        __width: private attr for the with of the Rectangle
        __height: private attr for the height of the Rectangle
    """
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle

        Raises:
            TypeError: width must be an integer or
                    height must be an intege
            ValueError: width must be >= 0 height must be >= 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        height function that returns the height of Rectangle

        Return:
            int: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the Rectangle

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: height must be an intege
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        width function that returns the width of Rectangle

        Return:
            int: width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the Rectangle

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: height must be an intege
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
