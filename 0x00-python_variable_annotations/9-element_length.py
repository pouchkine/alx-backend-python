#!/usr/bin/env python3

"""
typing a function
"""

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lst  iterable
    """
    return [(i, len(i)) for i in lst]
