#!/usr/bin/python3
"""
THIS Modual contains script  that adds all arguments to a
Python list, and then save them to a file
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_ = []
for i in range(1, len(sys.argv)):
    list_.append(sys.argv[i])
with open("add_item.json", encoding="utf-8", mode='w') as f:
    json.dump(list_, f, indent=2)
