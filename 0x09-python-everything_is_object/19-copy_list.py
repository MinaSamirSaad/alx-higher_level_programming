#!/usr/bin/python3
def copy_list(list_):
    return list_.copy() if (type(list_) is list or type(list_) is dict) else list_
