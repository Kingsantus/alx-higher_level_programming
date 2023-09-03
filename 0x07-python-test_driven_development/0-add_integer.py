#!/usr/bin/python3
""" 
add_integer module receives two args
this module adds two args provide
if args 1 or args 2 is not an int or float Raise TypeError
"""
def add_integer(a, b=98):
    """ return the sum a and b
    Raise:
        TypeError: if a is not int or b is not int """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
