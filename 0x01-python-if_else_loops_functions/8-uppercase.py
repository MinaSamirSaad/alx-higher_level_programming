#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in str:
       if (ord(i) >= ord('a') and ord(i) <= ord('z')):
        str1+= chr(ord(i) - 32)
    print(str1)
