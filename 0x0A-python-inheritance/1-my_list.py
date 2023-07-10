#!/usr/bin/python3
"""
MyList inherits from list
Public instance method: print_stored() that prints the sorted list
"""


class MyList(list):
    """
    Subclass MyList, superclass list
    """
    def print_sorted(self):
        print(sorted(self))
