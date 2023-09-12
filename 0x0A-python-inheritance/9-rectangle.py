#!/usr/bin/python3
""" 9-rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" BaseGeometry import"""
class Rectangle(BaseGeometry):
    """Rectangle class initializes all defined input """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
    def area(self):
        """method area multipy width by height"""
        return self.__width * self.__height

    def __str__(self):
        """str representation on print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
