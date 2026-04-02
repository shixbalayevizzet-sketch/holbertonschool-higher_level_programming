#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    If a key doesn't exist, the dictionary won't change.
    """
    # pop(key, None) deletes the key if it exists.
    # If the key is not found, it returns None instead of raising an error.
    a_dictionary.pop(key, None)
    return a_dictionary
