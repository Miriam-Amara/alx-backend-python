#!/usr/bin/env python3

"""

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], None]:
    """ """

    def multiply_num(num: float):
        print(num * multiplier)

    return multiply_num
