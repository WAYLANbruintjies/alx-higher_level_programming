#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
