#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if roman_string is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define Roman numeral values
    rom_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    n = len(roman_string)

    for i in range(n):
        # Get the value of the current symbol
        current_val = rom_val.get(roman_string[i], 0)

        # Look ahead: if there's a next symbol and its value is greater
        if i + 1 < n and rom_val.get(roman_string[i + 1], 0) > current_val:
            res -= current_val
        else:
            res += current_val

    return res
