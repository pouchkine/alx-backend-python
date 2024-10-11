#!/usr/bin/env python3

"""
return a function annotation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a callable fuction
    """

    def func(number: float) -> float:
        return multiplier * number
    return func
