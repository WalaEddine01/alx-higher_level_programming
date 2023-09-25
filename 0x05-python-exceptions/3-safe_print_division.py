#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = (a / b)
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
