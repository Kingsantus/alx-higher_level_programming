#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    n = len(argv)
    for i in range(1, n):
        add += int(argv[i])
    print("{}".format(add))
