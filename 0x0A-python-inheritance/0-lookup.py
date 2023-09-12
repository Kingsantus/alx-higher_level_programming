#!/usr/bin/python3
"""0-lookup module"""
def lookup(obj):
    """
    looks up the available attributes and methods of an object

    Args:
        obj: object to look up

    Return:
        the list of available dir in the obj
    """
    return dir(obj)
