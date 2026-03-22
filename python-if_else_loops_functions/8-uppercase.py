#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # If the character is between 'a' (97) and 'z' (122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Shift it to the uppercase range
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
