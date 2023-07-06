#!/usr/bin/env python3
"""
Defines a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float
by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float as argument and returns a function that multiplies a float
    by multiplier
    """
    def mult():
        """Multiplies a float by multiplier"""
        return multiplier * multiplier

    return mult
