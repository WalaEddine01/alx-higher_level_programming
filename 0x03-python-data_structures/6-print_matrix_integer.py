#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if i != matrix[0]:
            print()
        for j in i:
            if j != i[-1]:
                print(j, end=' ')
            else:
                print(j, end='')
    print()
