#!/usr/bin/python3


class Square:
    """
    This class represents a square.

    Attributes:
        dict_: dict, a dictionary to store square properties.
              The dictionary contains the following key-value pairs:
              - 'side_length': float, the length of each side of the square.
              - 'area': float, the area of the square calculated as side_length ** 2.
    """
    def __init__(self):
        """
        Initializes a Square instance.

        Parameters:
            None
        """
        self.dict_ = {}  # Initialize an empty dictionary for square properties

# Test the Square class
if __name__ == "__main__":

    """
    This instance allows us to control
    the pthon script at the execution
    """

    mysquare = Square()
    print(type(mysquare))
    print(mysquare.dict_)

