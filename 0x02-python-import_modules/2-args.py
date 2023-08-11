#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv)
    if n == 1:
        print("{} arguments.".format(n - 1))
    else:
        print("{} argument:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]), end='\n')
