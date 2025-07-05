#!/usr/bin/env python3

"""

"""

from typing import TypeVar, Any

K = TypeVar("K")
V = TypeVar("V")


def safely_get_value(
    dct: dict[K, V], key: K, default: Any | None = None
) -> V | Any | None:
    """ """

    if key in dct:
        return dct[key]
    else:
        return default
