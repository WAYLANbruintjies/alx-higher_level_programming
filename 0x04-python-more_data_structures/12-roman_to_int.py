#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub = sub + n

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    _roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(_roman_val.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if _roman_val.get(char) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [_roman_val.get(char)]
                else:
                    list_num.append(_roman_val.get(char))

                last_rom = _roman_val.get(char)

    num += to_subtract(list_num)

    return (num)
