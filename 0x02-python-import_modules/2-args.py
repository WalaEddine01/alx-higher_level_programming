#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} argument:".format(len(sys.argv) - 1))
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i = i + 1
