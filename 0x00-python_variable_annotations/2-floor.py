#!/usr/bin/env python3

"""
This module provides a function to return the floor of a floating-point number.
"""


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    num = str(n).split(".")
    return int(num[0])
