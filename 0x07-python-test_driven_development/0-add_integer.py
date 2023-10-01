#!/usr/bin/python3
'''
This modual contains add_integer
and importing the doctest modual
to test the function
'''


def add_integer(a, b=98):
    """
    This function adds two integers and return the sum

    Args:
        a: the first input
        b: the second input

    Return:
        the sum of them

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if type(a) not in {int, float}:
        raise TypeError("a must be an integer")
    if type(b) not in {float, int}:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
