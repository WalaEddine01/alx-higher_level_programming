#!/usr/bin/python3
"""
Thid modual contains the from_json_string functioon
"""


def from_json_string(my_str):
    """
    This function returns an object (Python data structure) represented by a
    JSON string

    Args:
        my_str: the json string
    """
    import json

    return json.loads(my_str)
