#!/usr/bin/python3
"""2-append_write module """
def append_write(filename="", text=""):
    """apend_write() append text in the filename"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
