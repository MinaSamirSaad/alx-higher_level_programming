#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for i in range(2):
        if i <len(tuple_a):
            result[i] += tuple_a[i]
        if i <len(tuple_b):
            result[i] += tuple_a[i]
    return tuple(result)
