#!/usr/bin/python3
def islower(c):
    if c == c.lower() and ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
