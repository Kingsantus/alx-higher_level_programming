#!/usr/bin/python3
"""100-my_int"""
class MyInt(int):
    """Myint class"""
    def __init__(self, value):
        """Instantiates object"""
        self.value = value
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

