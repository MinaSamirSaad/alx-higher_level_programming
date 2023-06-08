#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    length = len(argv)
    if len < 4 :
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = argv[1]
    b = argv[3]
    match argv[2]:
        case '+':
            print("{:d} + {:d} = {:d}".format(a,b,add(a,b)))
            exit(0)
        case '-':
            print("{:d} - {:d} = {:d}".format(a,b,sub(a,b)))
            exit(0)
        case '*':
            print("{:d} * {:d} = {:d}".format(a,b,mul(a,b)))
            exit(0)
        case '/':
            print("{:d} / {:d} = {:d}".format(a,b,div(a,b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
