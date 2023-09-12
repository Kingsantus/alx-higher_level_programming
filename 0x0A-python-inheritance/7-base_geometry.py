#!/usr/bin/python3
"""7-base_geometry module """
class BaseGeometry:
    """ BaseGeometry class area func not defined, throw error when area is intracted with """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator ensure value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
