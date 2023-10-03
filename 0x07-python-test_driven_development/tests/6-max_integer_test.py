#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class to make the TestCases for the max_integer fucntion
    """
    def test_empty(self):
        """
        This function to test case if the list empty
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """
        This function to test case if the list contains one elem
        """
        self.assertEqual(max_integer([1]), 1)

    def test_max(self):
        """
        This function to test case if the max at the end
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_neg(self):
        """
        This function to test case if the elements are neg
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max_mid(self):
        """
        This function to test case if the max in the mid
        """
        self.assertEqual(max_integer([1, 4, 3]), 4)

    def test_max_beg(self):
        """
        This function to test case if the max in the beg
        """
        self.assertEqual(max_integer([5, 2, 3]), 5)

    def test_str_err(self):
        """
        This function to test case if the list contains string elem
        """
        self.assertRaises(TypeError, max_integer, [2, 1, "d"])


if __name__ == "__main__":
    import unittest
    unittest.main()
