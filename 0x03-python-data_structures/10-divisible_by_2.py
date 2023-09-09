#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            list2.append(True)
        else:
            list2.append(False)
    return list2
