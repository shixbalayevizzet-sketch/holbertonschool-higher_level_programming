#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    """
    # Simply assigning the value to the key handles both
    # replacing an existing key and adding a new one.
    a_dictionary[key] = value
    return a_dictionary
