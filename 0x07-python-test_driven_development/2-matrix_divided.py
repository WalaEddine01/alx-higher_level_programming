#!/usr/bin/python3
"""
This modual contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    This function returns the new matrix with its elements are devided
    on 'div'

    Args:
        matrix: the matrix
        div: the variable that should devide on

    Raises:
        TypeError: if the matrix is not a list or the elements are not integers
        or floats, or the size if rows are deffrent.
        ZeroDivisionError: if "div" is equal to zero

    Return: the new matrix
    """
    if type(div) not in {float, int}:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        for j in i:
            if type(j) not in {float, int}:
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have\
the same size")
    mat2 = list(map(lambda row: list(map(lambda var: var / div, row)), matrix))
    mat2 = list(
            map(lambda row: list(map(lambda var: round(var, 2), row)), mat2)
            )
    return mat2


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
