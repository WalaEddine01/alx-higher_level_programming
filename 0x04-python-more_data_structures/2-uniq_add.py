#!/usr/bin/python3
def uniq_add(my_list=[]):
    b, a, c = 0, 0, 0
    for i in my_list[:]:
        a = 0
        c = 0
        for j in my_list[:]:
            if i == j:
                continue
            elif my_list[i] == my_list[j] and a > 0:
                c = 1
                break
            elif my_list[i] == my_list[j]:
                a = a + 1
        if c != 1:
            b = b + my_list[i]
    return b
