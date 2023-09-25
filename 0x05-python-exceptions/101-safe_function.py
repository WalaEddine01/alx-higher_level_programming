#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
        return result
    except Exception as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return result
