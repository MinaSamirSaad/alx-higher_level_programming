#!/usr/bin/python3
def fizzbuzz():
    str = ''
    for i in range(1, 101):
        if (i % 15 == 0):
            str = 'FizzBuzz'
        elif (i % 5 == 0):
            str = 'Buzz'
        elif (i % 3 == 0):
            str = 'Fizz'
        else:
            str = i
        print(str, end=' ')
