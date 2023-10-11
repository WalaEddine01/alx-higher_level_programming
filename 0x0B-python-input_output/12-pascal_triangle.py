#!/usr/bin/python3
"""
This modual contains the pascal_triangle function
"""


def pascal_triangle(n):
    '''
    pascal_triangle function that return a list of a list contains
    the pascal triangle

    Args:
        n: the number lines
    '''
    list_ = []
    list_2 = []
    if n <= 0:
        return list_
    for i in range(n):
        for j in range(i + 1):
            if j == i or j == 0:
                list_.append(1)
            else:
                list_.append(list_2[i - 1][j] + list_2[i - 1][j - 1])
        list_2.append(list_)
        list_ = []
    return list_2
