#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] < my_list[j]: 
                break
            if j == len(my_list) - 1: 
                return my_list[i]
