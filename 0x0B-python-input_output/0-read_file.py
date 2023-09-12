#!/usr/bin/python3
""" 0-read_file module """
def read_file(filename=""):
    """ read_file function open a file, read through and print out """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
