#!/usr/bin/python3
"""
This modual contains append_after function
"""
def append_after(filename="", search_string="", new_string=""):
    """
    append_after function that inserts a line of text to a file,
    after each line containing a specific string 

    Args:
        filename: the name of the file
        search_string: the searching string
        new_string: the new string
    """
    with open(filename, encoding="utf-8", mode="r") as f:
        a = 0
        data = f.readlines()
        for i in range(len(data)):
            i += 1
            if a == 1:
                data.insert(i, new_string)
                a = 0
            elif search_string in data[i]:
                a = 1
    with open(filename, encoding="utf-8", mode="w") as f:
        my_string = ''.join(data)
        f.write(my_string)
