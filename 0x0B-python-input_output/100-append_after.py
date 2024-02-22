#!/usr/bin/python3
"""13. Search and update #advanced"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file\
    after each line containing a specific string
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w', encoding='utf-8') as x:
        x.write(text)
