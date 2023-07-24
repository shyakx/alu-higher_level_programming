#!/usr/bin/python3
'''creating a class called Square'''


class Square:
    '''Initializing a special method __init__'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >=0")
