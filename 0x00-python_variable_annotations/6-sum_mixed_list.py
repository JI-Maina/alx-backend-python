#!/usr/bin/env python3
"""
Defines a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list of integers and floats and returns their sum as a float
    """

    sum: float = 0.0
    for item in mxd_lst:
        sum = item + sum

    return sum
