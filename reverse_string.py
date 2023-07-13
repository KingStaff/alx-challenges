#!/usr/bin/python3
"""
a module to reverse a string in python
"""

def reverse_string(s):
    """
    a function to reverse a given string
    s: is the string to be given
    returns s
    """
    result = ""

    if type(s) is not str:
        raise TypeError("s must be a string")

    if s == "":
        return ""
    else:
        for c in s:
            result = c + result

    return result
