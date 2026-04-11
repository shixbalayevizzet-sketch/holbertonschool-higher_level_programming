#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            # We only catch errors related to the type/format, not the index
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return printed_count
