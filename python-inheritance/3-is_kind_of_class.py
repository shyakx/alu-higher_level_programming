#!/usr/bin/python3
''' function declaration'''


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class; otherwise False."""
    return isinstance(obj, a_class)
