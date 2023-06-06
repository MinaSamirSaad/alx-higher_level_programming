#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if (i % 2 != 0):
        print('{:c}'.format(i - ord('a') + ord('A')), end='')
    else:
        print('{:c}'.format(i), end='')
