#!/usr/bin/python3
"""square module"""
class Square():
    """square class"""
    def __init__(self, size=0):
        """initialization of instance"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = size

    """area method"""
    def area(self):
        """public instance"""
        return self.__size ** 2
