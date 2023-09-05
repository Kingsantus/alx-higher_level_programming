#!/usr/bin/python3
"""Rectangle module
"""

class Rectangle:
    """Rectangle class accepts two argument
    use setter and method to return value
    Return the value of each args"""

    number_of_instances = 0
    print_symbol = "#"
    """number of instance initialized and recorded each time"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of a rectangle length * height"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of a rectangle 2(length + height)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """turn height to #
        return # * width"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """return width and height"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """remove instance and return print()"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """if condition is meet will return biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance width and height size"""
        return cls(size, size)
