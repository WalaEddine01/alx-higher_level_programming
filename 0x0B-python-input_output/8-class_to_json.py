#!/usr/bin/python3
"""
This modual contains the calss_tojson function
"""


def class_to_json(obj):
    """
    this functionconverts a class data to json obj

    Args:
        obj: the class obj
    """
    import json
    data = json.dumps(obj.__dict__)
    return json.loads(data)
