#!/usr/bin/python3
# manual reverse
def print_reversed_list_integer(my_list=[]):
    if my_list:
        index = len(my_list) - 1
        while (index >= 0):
            print('{:d}'.format(my_list[index]))
            index -= 1
