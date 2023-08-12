#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    second = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    result = (first[0] + second[0], first[1] + second[1])
    return result
