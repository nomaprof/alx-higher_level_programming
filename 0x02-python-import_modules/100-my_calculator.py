#!/usr/bin/python3

if __name__ == "__main__":
    """my little calculator"""
    import sys

    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    sym = sys.argv[2]
    if sym != '+' and sym != '-' and sym != '*' and sym != '/':
        print("Unknown operator. Available operators: +. -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sym == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sym == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sym == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
