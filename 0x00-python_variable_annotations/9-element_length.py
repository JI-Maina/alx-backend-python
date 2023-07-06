#!/usr/bin/env python3
"""
Annotate below function’s parameters, return values with  appropriate types
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a tuple with an item and len of item
    """
    return [(i, len(i)) for i in lst]
