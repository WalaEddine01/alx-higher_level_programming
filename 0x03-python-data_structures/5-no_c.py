#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for i in range(0, my_string.count("c")):
        my_string.remove("c")
    for i in range(0, my_string.count("C")):
        my_string.remove("C")
    my_string = "".join(my_string)
    return my_string
