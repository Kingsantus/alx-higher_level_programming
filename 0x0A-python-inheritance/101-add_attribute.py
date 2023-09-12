#!/usr/bin/python3
"""101-add_attribute module"""
def add_attribute(obj, attr, value):
    """ adds attribute to an object if it is possible
    Args:
        obj: object to receive new attributes
        attr: attribute name
        value: attribute value

    Raise(s):
        TypeError: if new attribute can't be added"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
