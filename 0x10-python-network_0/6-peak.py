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
    elif len(list_of_integers) < 3:
        return max(list_of_integers)

    return max(list_of_integers[1:-1])
