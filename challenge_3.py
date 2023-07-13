"""
This module counts the unique elements of a list
"""


def count_unique_elements(arr):
    """
    The function count_unique_elements counts
    the number of unique elements of a list

    Args:
        arr (list)

    >>> count_unique_elements([1, 2, 3, 4, 6])
    5
    >>> count_unique_elements([1, 2, 6, 4, 6])
    3
    >>> count_unique_elements([6, 2, 6, 6, 6])
    1
    >>> count_unique_elements([6, 6, 6, 6, 6])
    0
    >>> count_unique_elements([3, 2, -3, 6, -6])
    5
    >>> count_unique_elements([3])
    1
    >>> count_unique_elements(["3", "5", "8"])
    Traceback (most recent call last):
    ...
    TypeError: Input must be a list of integers
    >>> count_unique_elements([3, 5, "8"])
    Traceback (most recent call last):
    ...
    TypeError: Input must be a list of integers
    >>> count_unique_elements(3)
    Traceback (most recent call last):
    ...
    TypeError: Input must be a list of integers
    >>> count_unique_elements()
    Traceback (most recent call last):
    ...
    TypeError: count_unique_elements() missing 1 required positional argument: 'arr'
    """
    if type(arr) is not list:
        raise TypeError("Input must be a list of integers")
    u_count = 0
    for number in arr:
        if type(number) is not int:
            raise TypeError("Input must be a list of integers")
        if arr.count(number) == 1:
            u_count += 1
    return u_count
