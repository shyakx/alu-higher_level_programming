#!/usr/bin/python3
''' creating a class called Square '''


class Square:
    '''Initializing a special method __init__'''
    def __init__(self, size = 0):
        ''' giving a condition to check the if size is integer '''
        if not isinstance(size, int):
            ''' here it will raise a type error if size is not integer '''
            raise TypeError("size must be an integer")
        ''' giving a condition to check if size if negative and it raise an error'''
        if size < 0:
            ''' here it will raise ValueError '''
            raise ValueError("size must be >= 0")
        ''' variable creation '''
        self.__size = size
    def area(self):
        return self.__size
