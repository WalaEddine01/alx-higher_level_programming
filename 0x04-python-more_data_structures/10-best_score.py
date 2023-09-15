#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxe = 0
    a = 0
    for i, j in a_dictionary.items():
        if j > maxe:
            maxe = j
            a = i
    if (a == 0):
        return None
    return a
