#!/usr/bin/python3
def no_c(my_string):
    copy_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            copy_string += i
    return copy_string
