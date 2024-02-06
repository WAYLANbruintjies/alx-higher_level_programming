#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""

    try:
        dvsn = a / b
    except (TypeError, ZeroDivisionError):
        dvsn = None
    finally:
        print("Inside result: {}".format(dvsn))
    return (dvsn)
