#!/usr/bin/python3
"""
Thid modual contains the read_file functioon
"""


def read_file(filename=""):
    """
    this function reads a file and print its content

    Args:
        filename: the name if the file
    """
    with open(filename, encoding="utf-8", mode="r") as f:
        file_ = f.read()
    print(file_, end="")
