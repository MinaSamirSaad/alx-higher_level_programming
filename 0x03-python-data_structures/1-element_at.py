#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx >= len(my_list) or len(my_list) == 0):
        return None
    return my_list[idx]
