#!/usr/bin/python3
'''create aclass '''


class BaseGeometry:
    """
    A class representing a base geometry.
    Public instance method:
    - area(self): Raises an Exception
    """
     def area(self):
        """
        Raises an Exception 
        """
        raise Exception("area() is not implemented.")
