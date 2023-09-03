#!/usr/bin/python3
"""
print_square module
this module receives args
multipy # by args
if args is not an int or float raise TypeError
if args is less than 0 raiseVvalueError
"""
def print_square(size):
    """
    print # * size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
