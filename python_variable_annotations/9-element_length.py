#!/usr/bin/env python3
"""Type-annotated function to_kv module."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a string k and an int or float v as arguments"""
    return [(i, len(i)) for i in lst]
