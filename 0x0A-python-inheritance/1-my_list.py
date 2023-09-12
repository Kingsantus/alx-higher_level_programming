#!/usr/bin/python3
""" 1-my_list module"""
class MyList(list):
    """Mylist class takes in list as argument
    the list argument is sorted in the method 
    print the sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
