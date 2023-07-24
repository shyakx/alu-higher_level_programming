#!/usr/bin/python3
'''create a class'''


class Square:
    '''Initializing a special method __init__ '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    '''setting size'''
    @size.setter
    def size(self, value):
        '''condition to make size integer otherwise gives typeerror'''
        if not isinstance(value, int):
            '''raising of error with message'''
            raise TypeError("size must be an integer")

        ''' condition to make size positive'''
        if value < 0:
            '''raising of value error'''
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
    '''another pubic instance to print #'''
    def my_print(self):
        if size = 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
