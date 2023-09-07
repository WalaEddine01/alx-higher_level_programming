#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = 0
    for i in sys.argv[1:]:
        a = int(i) + a
    print(a)
