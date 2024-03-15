#!/usr/bin/env python3
"""
9-element_length module
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns an elements length
    """
    return [(i, len(i)) for i in lst]
