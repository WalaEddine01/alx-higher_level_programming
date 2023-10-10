#!/usr/bin/python3
"""
Thid modual contains the read_file functioon
"""


def append_write(filename="", text=""):
    """
    this function append a file and return the number of the characters

    Args:
        filename: the name if the file
        text: the text have to write on the file
    """
    with open(filename, encoding="utf-8", mode="a") as f:
        a = f.write(text)
    return a
