#!/usr/bin/python3
def copy_list(l):
    return l.copy() if (type(l) == list or type(l) == dict) else l
