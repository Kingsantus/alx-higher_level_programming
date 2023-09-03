#!/usr/bin/python3
"""
say_my_name module concantenate two Args with a space
if agrs is not string raise TypeError
if only one args provide print else case
if both argument is provide print if case
"""
def say_my_name(first_name, last_name=""):
    """say_my_name() receives to arg
    concatenate and print
    if one arg print too"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        full_name = f"My name is {first_name} {last_name}"
    else:
        full_name = f"My name is {first_name}"
    print(full_name)
