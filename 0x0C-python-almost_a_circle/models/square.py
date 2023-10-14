#!/usr/bin/python3
"""
This class contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class That inhirits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        this method returns a string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        This is the getter method
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        this is the setter method
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        This is the uptade method
        That updates the value of the attr
        """
        if args:
            for arg, attr in zip(args, vars(self)):
                setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns a dictionary representation of a Square
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
