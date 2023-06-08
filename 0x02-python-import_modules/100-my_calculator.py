#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}
    op = argv[2]
    if op not in ops.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    num1, num2 = int(argv[1]), int(argv[3])
    print('{:d} {} {:d} = {:d}'.format(num1, op, num2, ops[op](num1, num2)))
