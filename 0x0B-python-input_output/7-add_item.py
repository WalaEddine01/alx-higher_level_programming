#!/usr/bin/python3
"""
THIS Modual contains script  that adds all arguments to a
Python list, and then save them to a file
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_ = []
for i in range(1, len(sys.argv)):
    list_.append(sys.argv[i])
save_to_json_file(list_, "add_item.json")
load_from_json_file("add_item.json")
