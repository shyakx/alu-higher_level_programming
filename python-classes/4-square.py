#!/usr/bin/python3
'''create a class'''

class Square:
    '''property getter'''
    def size(self):
        return self.__size
    '''property setter'''
    def def size(self, value):
        '''making sure size is integer'''
        if not isinstance(size, int):
            '''an error to raise'''
            raise TypeError("size must be an integer")
        '''making sure size is positive integer'''
        if size < 0:
            ''' Error to raise '''
            raise ValueError("size must be >= 0")
    
    '''instantation'''
    def __init__(self, size=0):
        self.__size = size

    '''public instance method that returns current square area'''
    def area(self):
        return self.__size ** 2

    def get_size(self):
        return self.__size
