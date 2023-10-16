#!/usr/bin/python3
"""
This modual contains methods to test Square class
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Tests the Base class
    """

    def setup(self):
        """
        Imports module, instantiates class
        """
        Base._Base__nb_objects = 0

    def test_cls(self):
        """
        Tests Square class type
        """
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")


if __name__ == "__main__":
    unittest.main()
