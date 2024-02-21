#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open("my_file_0.txt", "r", encode="utf-8") as f:
        return(f)
