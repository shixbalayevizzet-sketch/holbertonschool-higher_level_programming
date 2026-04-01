#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    """
    # Use the symmetric difference operator (^)
    # This finds elements that are in set_1 OR set_2, but NOT in both
    return set_1 ^ set_2
