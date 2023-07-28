#!/usr/bin/python3
'''
create a function '''


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    Parameters:
        obj (object): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
