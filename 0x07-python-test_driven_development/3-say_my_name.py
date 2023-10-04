#!/usr/bin/python3
"""
This is say_my_name modual contains ay_my_name function
"""
def say_my_name(first_name, last_name=""):
    """
    this is ay_my_name function prints My name is {first_name} {last_name}
    message
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
