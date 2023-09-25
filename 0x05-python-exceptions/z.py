#!/usr/bin/python3
try:
    raise TypeError  # This will raise a TypeError
except TypeError as te:
    print("An error occurred:")
