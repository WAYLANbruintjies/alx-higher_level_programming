#!/usr/bin/env python3
# File: 5-no_c.py

def no_c(my_string):
    """A function that removes all characters c and C from a string."""
     if my_string[]:
         new = my_string.translate({ord ("c"): None})
         alt_string = new.translate({ord ("c"): None})
         return alt_string
     return my_string
