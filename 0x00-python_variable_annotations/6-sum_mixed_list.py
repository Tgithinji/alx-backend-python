#!/usr/bin/env python3
"""
6-sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of mixed integers and floats and
    returns their sum as floats
    """
    return sum(mxd_lst)
