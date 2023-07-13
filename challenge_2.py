"""
This module counts the vowels in a string
"""


def count_vowels(s=""):
    """
    Function count_vowels returns n of vowels in a given string

    Args:
        s (str): default ""

    >>> count_vowels("hello")
    2
    >>> count_vowels("ttyl")
    0
    >>> count_vowels("aoi")
    3
    >>> count_vowels("HELLO")
    2
    >>> count_vowels("TTYL")
    0
    >>> count_vowels("AIO")
    3
    >>> count_vowels("HELlo")
    2
    >>> count_vowels("TtYl")
    0
    >>> count_vowels("AoIu")
    4
    >>> count_vowels("")
    0
    >>> count_vowels()
    0
    >>> count_vowels("123")
    0
    >>> count_vowels(123)
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string
    >>> count_vowels(["hola", "soy", "dora"])
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string
    >>> count_vowels(["Hola"])
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string

    """
    if type(s) is not str:
        raise TypeError("Input must be a string")
    vowels = "aeiou"
    v_count = 0
    for letter in s:
        if letter.lower() in vowels:
            v_count += 1
    return v_count
