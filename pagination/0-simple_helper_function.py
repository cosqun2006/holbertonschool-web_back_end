#!/usr/bin/python3
"""
Simple helper function to calculate pagination index range.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
