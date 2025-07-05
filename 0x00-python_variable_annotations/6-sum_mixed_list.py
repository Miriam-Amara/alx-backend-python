#!/usr/bin/env python3

"""
This module provides sum_mixed_list function that calculates
the sum of a list containing both integers and floats.
"""


def sum_mixed_list(mxd_list: list[int | float]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.

    Args:
        mxd_list (list[int | float]): A list of numbers
                                        (integers and/or floats).

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    result = sum(mxd_list)
    return float(result)
