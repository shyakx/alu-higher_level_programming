#!/usr/bin/python3
''' dec of function'''


def inherits_from(obj, a_class):
     """Returns True if obj is an instance of a class inherited"""
      return isinstance(obj, type) and issubclass(type(obj), a_class) and type(obj) != a_class
