#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    If no score found, return None.
    """
    # Check if the dictionary is empty or None
    if not a_dictionary:
        return None
    # Use max() with the dictionary's values to find the key
    # that has the highest value
    return max(a_dictionary, key=a_dictionary.get)
