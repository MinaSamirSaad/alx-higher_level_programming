#!/usr/bin/python3
''' base class module '''
import json
import csv


class Base:
    ''' class base

        Attributes:
            private class att : nb_objects (int)
            public instance att : id (int)
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' base constructor '''
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' convert list of dict represent objects to json string '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' write to file list of objects as json '''
        if list_objs is None:
            x = []
        else:
            x = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__+'.json', 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        ''' return json string as list of dictionaries '''
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, *args, **dictionary):
        ''' create object and update it with dictionary '''
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        else:
            return None

        obj.update(*args, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' load json from file and convert to
        list of instances and return them'''
        json_list = []
        try:
            with open(cls.__name__+'.json', 'r', encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
        except Exception:
            return []

        return [cls.create(**s) for s in json_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' save to csv file '''
        x = None
        if list_objs is None:
            x = []
        else:
            x = [obj.to_dictionary() for obj in list_objs]

        x = [list(obj.values()) for obj in x]
        with open(cls.__name__+'.csv', 'w', encoding="utf-8") as f:
            csvwriter = csv.writer(f, lineterminator='\n')
            csvwriter.writerows(x)

    @classmethod
    def load_from_file_csv(cls):
        ''' load csv from file and convert to
        list of instances and return them'''
        csv_list = []
        try:
            with open(cls.__name__+'.csv', 'r', encoding="utf-8") as f:
                csvreader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for row in csvreader:
                    csv_list.append([int(i) for i in row])
        except Exception:
            return []
        return [cls.create(*s) for s in csv_list]
