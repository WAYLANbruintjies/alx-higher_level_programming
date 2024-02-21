#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns num bytes
    """
    with open(filename, mode='a', encoding='utf-8') as app_file:
        return(app_file.write(text))
