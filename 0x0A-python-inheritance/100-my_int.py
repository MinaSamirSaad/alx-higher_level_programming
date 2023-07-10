#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)  # Invert the result of the default `==` operator

    def __ne__(self, other):
        return super().__eq__(other)  # Invert the result of the default `!=` operator
