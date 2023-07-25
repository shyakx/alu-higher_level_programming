#!/usr/bin/python3
'''
creating a new class
'''


class Rectangle:
    """
    A class that represents a rectangle.

    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object with the given width and height.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        and raises type error when height is not
        integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if self.width == 0  or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        calculates and returns a triangle of # characters
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]
