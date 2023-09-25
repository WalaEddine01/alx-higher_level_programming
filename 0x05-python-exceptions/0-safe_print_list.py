#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for j in range(0, x):
            print(my_list[j], end="")
            i+=1
    except IndexError:
        print()
    else:
        print()
    return i
