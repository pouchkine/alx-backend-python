#!/usr/bin/env python3

"""
typing list of int and float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    mxd_lst ist alist with int and float
    """
    return(sum(mxd_lst))
