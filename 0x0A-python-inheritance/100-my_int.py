#!/usr/bin/python3
"""
Class MyInt
this class inherits from int and switch != and ==
"""


class MyInt(int):
    """ class that switch != and == """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
