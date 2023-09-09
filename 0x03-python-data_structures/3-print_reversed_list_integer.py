#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("the list is empty")
    elif len(my_list) == 1:
        for i in my_list:
            print("{:d}".format(i))
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
