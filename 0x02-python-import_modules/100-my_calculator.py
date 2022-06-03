#!/usr/bin/python3
import calculator_1 as calc
import sys
arg = sys.argv
length = len(arg)
operators = ['+', '-', '*', '/']
if __name__ == "__main__":
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(arg[1])
    operator = arg[2]
    b = int(arg[3])
    if arg[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == '+':
        res = calc.add(a, b)
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == '-':
        res = calc.sub(a, b)
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == '*':
        res = calc.mul(a, b)
        print("{} {} {} = {}".format(a, operator, b, res))
    elif operator == '/':
        res = calc.div(a, b)
        print("{} {} {} = {}".format(a, operator, b, res))
