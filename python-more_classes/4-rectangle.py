#!/usr/bin/python3

'''
create a class

'''

class Rectangle:
    '''
    Initialization of special method
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.width = value

    '''
    Public instance to return area
    '''
    def area(self):
        return self.width * self.height
    '''
    Public instance to return perimeter
    '''
    def perimeter(self):
        if self.width < 0 or self.height < 0:
            return 0
        return 2 * (self.width + self.height)
    '''
    __repr__
    '''
    def __str__(self):
        if self.width < 0 or self.height < 0:
            return ""
        rectangle_str = ""

        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"

        return rectangle_str[:-1]
    '''
    __repr__
    '''
    def __repr__ (self):
        return "Rectangle({}, {})".format(self.width, self.height)
