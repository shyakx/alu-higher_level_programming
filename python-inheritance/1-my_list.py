#!/usr/bin/python3
'''
create a subclass that inherits from list 
class
'''

class MyList(list):
    """
    MyList class is a subclass of list that allows printing the list in sorted (ascending) order.

    Public instance method:
    - print_sorted(self): Prints the list in ascending order (sorted).
    """
    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).
        """
        sorted_list = sorted(self)
        print(sorted_list)

