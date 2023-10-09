#!/usr/bin/python3
"""
This modual contains the BaseGeometry class
"""


class BaseGeometry:
    """
    this is BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function that validates value

        Args:
            name (str): the name
            value (int):  the value

        Raises:
            TypeError: {name} must be an integer
            ValueError: {name} must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
