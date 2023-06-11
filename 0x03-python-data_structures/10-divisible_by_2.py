#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_list = my_list[:]
    for i in range(len(copy_list)):
        copy_list[i] = True if my_list[i] % 2 == 0 else False
    return copy_list
