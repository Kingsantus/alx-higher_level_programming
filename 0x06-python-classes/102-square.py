#!/usr/bin/python3
"""square module"""
class Square():
    """Square class"""
    def __init__(self, size=0):
        """initialization of attr"""
        self.__size = size

    """setter method initialized"""
    @property
    def size(self):
        """get metthod for the size attr"""
        return self.__size

    """getter method initializes"""
    @size.setter
    def size(self, value):
        """set method for size attr"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = value

    """public method initiazied"""
    def area(self):
        """public instance to return square"""
        return self.__size ** 2

    def __lt__(self, other):
        """less than compare"""
        return self.area() < other.area()

    def __le__(self, other):
        """equal to or greater compare"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """equal compare"""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal to """
        return self.area() != other.area()

    def __gt__(self, other):
        """ greater than compare"""
        return self.area() > other.area()

    def __ge__(self, other):
        """less than or eeual to """
        return self.area() >= other.area()
