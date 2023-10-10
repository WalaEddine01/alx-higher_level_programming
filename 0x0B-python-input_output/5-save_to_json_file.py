#!/usr/bin/python3
"""
Thid modual contains the from_json_string functioon
"""


def save_to_json_file(my_obj, filename):
    """
    This function that writes an Object to a text file, using
    a JSON representation

    Args:
        my_obj: the text
        filename: the name of the file
    """
    import json
    with open(filename, encoding="utf-8", mode="w") as f:
        json.dump(my_obj, f)
