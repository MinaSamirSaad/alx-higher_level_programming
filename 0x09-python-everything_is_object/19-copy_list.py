#!/usr/bin/python3
def copy_list(list_):
    return list_.copy() if (type(list_) == list or type(list_) == dict) else list_
