#!/usr/bin/python3
"""7. Load, add, save"""

import sys
import json

if __name__ == "__main__":
    save_to_json_file = \
            __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    with open(filename, mode='a+', encoding='utf-8') as f:
        if f.tell == 0:
            json.dump([], f)
    data = load_from_json_file("add_item.json")
    if len(sys.argv > 1):
        data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")
