#!/usr/bin/env python3
"""Type-annotated function to_kv module."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int or float v as arguments"""
    return (k, float(v**2))
