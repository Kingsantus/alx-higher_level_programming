#!/usr/bin/python3
""" 8-rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" BaseGeometry import"""
class Rectangle(BaseGeometry):
    """Rectangle class initializes all defined input """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
