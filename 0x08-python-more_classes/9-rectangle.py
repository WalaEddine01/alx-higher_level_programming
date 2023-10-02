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
        number_of_instances: counter for instantiation and deletion of
        instance
        print_symbol: the simpol tha should print rectangle with
    """
    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        This function returns the area of a Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        This function returns the perimeter of a Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Generates a string representing of the rectangle.

        Return:
            str: A string with "Rectangle.print_symbol" characters representing
            the rectangle's shape.
        """
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """
        Returns a string representing of the Rectangle obj

        Return:
            str: a string in the format Rectangle(width, height)
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        Destroy the Rectangle class and prints "Bye rectangle..."
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This static method to test is the first instance is bigger
        or the second

        Args:
            rect_1: the first input
            rect_2: the second input

        Raises:
            TypeError: rect_1 and rect_2 must be an instance of Rectangle

        Return:
            the instance hase biggest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
