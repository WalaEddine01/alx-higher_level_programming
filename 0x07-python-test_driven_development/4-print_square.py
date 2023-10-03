#!/usr/bin/python3
"""
This modual contains print_square function
"""


def print_square(size):
    if type(size) is not int or type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
