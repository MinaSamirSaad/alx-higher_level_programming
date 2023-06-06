#!/usr/bin/python3
def uppercase(str):
    char = ''
    for i in str:
       if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            char = ord(i) - ord('a') + ord('A')
            print('{:c}'.format(char), end='')
print('')
