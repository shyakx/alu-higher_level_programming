#!/usr/bin/python3
'''
creating a new class
'''


class Rectangle:
    '''
    Initializition of special method
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    '''
    private instance width
    '''
    @property
    def width(self):
        return self.__width
    '''
    private instance width setter
    '''
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        return self.__width

    '''
    private instance height
    '''
    @property
    def height(self):
        return self.__height
    '''
    private instance heifht setter
    '''
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        return self.__height
