#!/usr/bin/env python3
"""
8-make_multiplier module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    parameters:
    multiplier: float
        a number to multiplier

    returns:
        a function that multiplies the multiplier with a float
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
