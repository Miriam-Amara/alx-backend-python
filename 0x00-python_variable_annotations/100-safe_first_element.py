#!/usr/bin/env python3

"""

"""
from typing import Any


# The types of the elements of the input are not know
def safe_first_element(lst: list[Any]) -> list[Any] | None:
    if lst:
        return lst[0]
    else:
        return None
