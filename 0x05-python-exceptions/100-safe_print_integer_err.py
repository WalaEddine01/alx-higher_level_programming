#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return False
