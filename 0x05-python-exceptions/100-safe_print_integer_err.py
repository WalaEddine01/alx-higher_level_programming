#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    a = True
    try:
        print("{:d}".format(value))
    except Exception as te:
        print("Exception: {}".format(te), file=sys.stderr)
        a = False
    return a
