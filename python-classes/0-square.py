#!/usr/bin/python3


class Square:
    """
    This class represents a square.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self):
        """
        Initializes a Square object.
        """
        self.dict_ = {}

# Test case
if __name__ == "__main__":
    mysquare = Square()
    print(type(mysquare))  # Output: <class '__main__.Square'>
    print(mysquare.dict_)  # Output: {}
