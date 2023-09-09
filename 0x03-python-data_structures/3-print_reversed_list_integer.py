#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list2 = my_list.copy()
    list2.reverse()
    for i in list2:
        print("{:d}".format(i))
