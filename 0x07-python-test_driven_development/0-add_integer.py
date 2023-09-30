#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is int and type(b) is int\
            or type(a) is float and type(b) is float\
            or type(a) is int and type(b) is float\
            or type(b) is int and type(a) is float:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(a)
        return a + b
    elif type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(a) is not int or type(a) is not float:
        raise TypeError("b must be an integer")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
