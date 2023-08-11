#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if len(sys.argv) != 4:
    print("Usage: python calculator.py <a> <operator> <b>")
    sys.exit(1)
try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

if sys.argv[2] == "+":
    result = add(a, b)
elif sys.argv[2] == "-":
    result = sub(a, b)
elif sys.argv[2] == "*":
    result = mul(a, b)
elif sys.argv[2] == "/":
    result = div(a, b)
else:
    print('Unknown operator. Available operators: +, -, * and /')
    sys.exit(1)


print("{} {} {} = {}".format(a, sys.argv[2], b, result))
sys.exit(0)
