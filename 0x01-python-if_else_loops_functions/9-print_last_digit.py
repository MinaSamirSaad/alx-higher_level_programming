#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if(num < 0):
        num *= -1
    num = num % 10
    print("{:d}".format(num), end='')
    return num
