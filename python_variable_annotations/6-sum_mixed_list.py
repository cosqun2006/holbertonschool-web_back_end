#!/usr/bin/env python3
"""This module provides a type-annotated function sum_mixed_list."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of a list of integers and floats and returns it as a float."""
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
