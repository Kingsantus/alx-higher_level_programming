#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    final = 0
    int_v = 0
    for i in reversed(roman_string):
        v = roman_num.get(i, 0)
        if v < int_v:
            final -= v
        else:
            final += v
        int_v = v
    return final
