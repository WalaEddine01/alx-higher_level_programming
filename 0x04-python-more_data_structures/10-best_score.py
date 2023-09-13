#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        maxe = 0
        a = 0
        for i in a_dictionary:
            if a_dictionary[i] > maxe:
                maxe = a_dictionary[i]
                a = i
        return a
