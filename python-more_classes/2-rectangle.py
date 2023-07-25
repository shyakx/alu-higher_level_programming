#!/usr/bin/python3
'''
creating a new class
'''


class Rectangle:
    '''
    Initialization of special method
    '''
    def __init__(self, width=0, height=0):
        self.width = width  # Use the setter to enforce checks
        self.height = height  # Use the setter to enforce checks

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    ''' private instance that return area '''
    def area(self):
        return self.__height * self.__width
    ''' public instance that returns permiter '''
    def perimeter(self):
        if height or width is < 0:
            return 0
        else:
            return 2*(self.__height + self.__width)
