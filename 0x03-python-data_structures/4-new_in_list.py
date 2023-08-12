#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied = my_list.copy()
    if idx < 0:
        return copied
    elif idx > len(copied) -1:
        return copied
    else:
        copied[idx] = element
        return copied
