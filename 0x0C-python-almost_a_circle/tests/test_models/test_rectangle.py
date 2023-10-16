#!/usr/bin/python3
"""
This modual contains methods to test Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_cls(self):
        """
        Tests Rectangle class type
        """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")


if __name__ == "__main__":
    unittest.main()
