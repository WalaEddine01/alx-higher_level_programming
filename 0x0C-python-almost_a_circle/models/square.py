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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
