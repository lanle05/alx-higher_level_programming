#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Print the dictionary with sorted keys
    for key in sorted_keys:
        value = a_dictionary[key]
        print('{}: {}'. format(keys, a_dictionary[keys]))
