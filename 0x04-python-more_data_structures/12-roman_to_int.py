#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return None
    a = 0
    number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        for j in number:
            if roman_string[i] == j:
                a += number[j]
                if i != 0 and \
                        number[roman_string[i]] > number[roman_string[i - 1]]:
                    a -= number[roman_string[i - 1]] * 2
    if a == 0:
        return None
    return a
