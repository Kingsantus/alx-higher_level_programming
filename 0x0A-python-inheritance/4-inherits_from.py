#!/usr/bin/python3
"""4-inherits_from module"""
def inherits_from(obj, a_class):
    """ inherits_from receives two args, and check if obj is inherited from a_class """
    return isinstance(obj, a_class) and type(obj) is not a_class
