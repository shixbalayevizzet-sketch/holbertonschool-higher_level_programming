#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.
    The original dictionary remains unchanged.
    """
    # Create a new dictionary where each key's value is multiplied by 2
    return {key: value * 2 for key, value in a_dictionary.items()}
