#!/usr/bin/python3

'''creating a class'''
class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Calculates the area of the square.
        my_print(): Prints the square using the character '#'.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'.

        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
