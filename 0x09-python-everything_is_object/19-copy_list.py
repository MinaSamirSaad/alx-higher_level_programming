#!/usr/bin/python3
def copy_list(list_):
    return list_.copy() if (isinstance(list_, list) or isinstance(list_, dict)) else list_
