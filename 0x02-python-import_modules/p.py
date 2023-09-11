#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import mul, add, div, sub
    import sys
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    print(len(sys.argv))
