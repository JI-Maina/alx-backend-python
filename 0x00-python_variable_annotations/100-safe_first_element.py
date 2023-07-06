#!/usr/bin/env python3
"""
Defines a function that returns first item of an iterable
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first item of a given iterable"""
    if lst:
        return lst[0]
    else:
        return None
