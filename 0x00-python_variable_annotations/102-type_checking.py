#!/usr/bin/python3

"""

"""
from typing import Any, Sequence


def zoom_array(lst: Sequence[Any], factor: int | float = 2) -> list[Any]:
    """ """
    zoomed_in: Sequence[Any] = [
        item for item in lst
        for _ in range(int(factor))
        ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
