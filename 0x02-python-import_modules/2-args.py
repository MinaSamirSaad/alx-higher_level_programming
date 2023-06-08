#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) -1
    if length == 1:
        print('1 argument.')
    else :
        print('{:d} arguments.'.format(length))
    for i in range(1,length +1):
        print('{:d}: {:s}'.format(i, sys.argv[i]))
