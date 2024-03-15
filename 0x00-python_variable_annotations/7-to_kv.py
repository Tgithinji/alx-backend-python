#!/usr/bin/env python3
"""
7-to_kv module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    converts a string and int/float to a tuple

    parameters:
    k: str
        a string
    v: Union[int, float]
         a float or string

    Returns:
        a tuple containing a string and a float
    """
    return (k, float(v ** 2))
