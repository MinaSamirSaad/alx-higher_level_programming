#!/usr/bin/python3
"""Class Base"""

import json


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)


    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        data = []
        for obj in list_objs:
            if isinstance(obj, Base):
                data.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string(data))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Arguments:
        @cls: current class
        @dictionary: can be thought of as a double pointer to a dictionary
        Returns:
        An instance with all attributes already set
        """
        opj = {}
        if cls.__name__ == "Rectangle":
            opj = cls(1, 1)
        elif cls.__name__ == "Square":
            opj = cls(1)
        opj.update(**dictionary)
        return opj
    
    @classmethod
    def load_from_file(cls):
        data = None
        instances = []
        with open(f"{cls.__name__}.json", 'r') as f:
            data = json.load(f)
        for obj in data:
            instances.append(cls.create(**obj))
        return instances
