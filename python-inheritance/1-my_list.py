#!/usr/bin/python3
'''
create a subclass that inherits from list class
'''


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).
        """
        sorted_list = sorted(self)
        print(sorted_list)
