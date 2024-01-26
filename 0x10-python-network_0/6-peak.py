#!/usr/bin/python3
'''
module to Find a peak
'''


def find_peak(list_of_integers):
    '''
    function that finds a peak in a list of unsorted integers.
    '''
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) <= 3:
        return max(list_of_integers)

    mid = int(len(list_of_integers) / 2)
    mid_element = list_of_integers[mid]
    before_mid = list_of_integers[mid - 1]
    after_mid = list_of_integers[mid + 1]
    if mid_element > before_mid and mid_element > after_mid:
        return mid_element
    if mid_element < before_mid:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
