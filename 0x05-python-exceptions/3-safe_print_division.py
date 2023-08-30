#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""

    try:
        divsn = a / b
    except (TypeError, ZeroDivisionError):
        divsn = None
    finally:
        print("Inside result: {}".format(divsn))
    return (divsn)
