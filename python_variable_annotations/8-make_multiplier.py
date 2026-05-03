#!/usr/bin/env python3
"""Type-annotated function to_kv module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a string k and an int or float v as arguments"""
    def multiplier_function(n: float) -> float:
        """Takes a string k and an int or float v as arguments"""
        return n * multiplier
    return multiplier_function
