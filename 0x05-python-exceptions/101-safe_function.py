#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely
    NOTE:
        fct: Function to execute
        args: Arguments for fct"""

    try:
        outcome = fct(*args)
        return (outcome)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
