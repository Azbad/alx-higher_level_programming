#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    ret = 0
    if my_list is None:
        my_list = []
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print()
    return ret
