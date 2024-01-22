#!/usr/bin/python3
# File: 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """A fiunction that adds 2 tuples."""
    tuple_new = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_new = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_new
