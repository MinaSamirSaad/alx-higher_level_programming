#!/usr/bin/python3
'''function def copy_list(l): that returns a copy of a list.'''

def copy_list(l):
    return l.copy() if type(l) == list or type(l) == dict else l
