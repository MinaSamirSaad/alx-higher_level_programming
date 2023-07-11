#!/usr/bin/python3

def pascal_triangle(n): 
    myList = []
    for i in range(1, n+1):
        li = []
        if len(myList) == 0:
            li.append(1)
        elif  len(myList) == 1:
            li.append(1)
            li.append(1)
        else:
            li.append(1)
            for j in range(1,len(myList[i -1])):
                li.append(myList[i -1][j] + myList[i -1][j-1])
            li.append(1)
        myList.append(li)
    return myList

pascal_triangle(5)