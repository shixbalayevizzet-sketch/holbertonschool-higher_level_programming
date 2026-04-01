#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    """
    # Create a set from the list to remove duplicates
    unique_integers = set(my_list)
    # Return the sum of the unique elements
    return sum(unique_integers)
