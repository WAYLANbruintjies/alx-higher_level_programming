#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns bytes (size)
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
