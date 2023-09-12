#!/usr/bin/python3
""" 1-write_file module """
def write_file(filename="", text=""):
    """ write_file function over write text in a file 
    return length of text"""
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
