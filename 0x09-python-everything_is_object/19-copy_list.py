#!/usr/bin/python3
def copy_list(list_):
    return list_.copy() if isinstance(list_, (list, dict)) else list_
