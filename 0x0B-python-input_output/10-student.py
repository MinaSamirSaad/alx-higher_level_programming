#!/usr/bin/python3
"""
Class Student
Public instance attributes:
- first_name
- last_name
- age
"""


class Student():
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        check if attrs is a list, if not retrieve None
        """
        if isinstance(attrs, list):
            for item in attrs:
                if not isinstance(item, str):
                    return self.__dict__
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__
