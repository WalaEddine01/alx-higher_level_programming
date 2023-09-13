#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    new = list(map(lambda row: list(map(lambda var: var**2, row)), matrix))
    return new
