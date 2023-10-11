#!/usr/bin/python3
"""
This modual contains append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: the name of the file
        search_string: the searching string
        new_string: the new string
    """
    with open(filename, encoding="utf-8", mode="r") as f:
        data = f.readlines()

    with open(filename, encoding="utf-8", mode="w") as f:
        for line in data:
            f.write(line)
            if search_string in line:
                f.write(new_string)
