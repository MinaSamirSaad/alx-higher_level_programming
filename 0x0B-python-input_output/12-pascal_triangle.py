#!/usr/bin/python3
'''
function that returns a list of lists of integers representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing the Pascal’s triangle of n
    Args:
        @n: number of lists of integers
    Return:
        list: list of lists of integers representing the Pascal’s triangle of n
    """
    myList = []
    if n <= 0:
        return myList
    for i in range(n + 1):
        li = []
        if i == 0:
            myList.append([1])
            continue
        li.append(1)
        for j in range(i - 1):
            sum = myList[i - 1][j] + myList[i - 1][j + 1]
            li.append(sum)
        li.append(1)
        myList.append(li)
    return myList
