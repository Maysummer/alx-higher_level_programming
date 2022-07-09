#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file"""


from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load('add_item.json')
except Exception:
    my_list = []

new_list = my_list + argv[1:]
save(new_list, 'add_item.json')
