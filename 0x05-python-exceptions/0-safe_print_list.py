#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list"""

    elm = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elm = elm + 1  #elm += 1
        except IndexError:
            break
    print("")
    return (elm)
