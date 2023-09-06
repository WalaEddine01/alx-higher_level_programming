#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    if (number.isnumeric() is True or number[0] == "-"):
        print(number[-1], end="")
        return (number[-1])
    else:
        print("TypeError")
