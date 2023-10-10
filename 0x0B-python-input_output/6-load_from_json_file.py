#!/usr/bin/python3
"""
This modual contains the load_from_json_file function
"""


def load_from_json_file(filename):
    import json
    """
    function  creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf=8", mode='r') as f:
        return json.load(f)
