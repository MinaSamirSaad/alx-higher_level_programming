#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or len(my_list) == 0 or my_list[idx] > len(my_list):
        return None
    return my_list[idx]
