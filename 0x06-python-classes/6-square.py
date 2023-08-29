#!/usr/bin/python3
"""square module"""
class Square():
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of attr"""
        self.__size = size
        self.__position = position

    """setter method initialized"""
    @property
    def size(self):
        """get metthod for the size attr"""
        return self.__size

    """getter method initializes"""
    @size.setter
    def size(self, size):
        """set method for size attr"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """Assign to private attr"""
        self.__size = size

    """setter method for position"""
    @property
    def position(self, value):
       """set position of value"""
       if not isinstance(value, tuple) or len(value) != 2:
           raise TypeError("position must be a tuple of 2 positive integers")
       elif not all(isinstance(i, int) and i >= 0 for i in value):
           raise TypeError("position must be a tuple of 2 positive integers")
       else:
           self.__position = value

    """public method initiazied"""
    def area(self):
        """public instance to return square"""
        return self.__size ** 2

    """public instance method"""
    def my_print(self):
        """prints a square using #"""
        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
