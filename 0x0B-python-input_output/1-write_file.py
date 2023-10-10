#!/usr/bin/python3
"""
Thid modual contains the read_file functioon
"""


def write_file(filename="", text=""):
    """
    this function reads a file and print its content

    Args:
        filename: the name if the file
        text: the text have to write on the file
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        a = f.write(text)
    return a
