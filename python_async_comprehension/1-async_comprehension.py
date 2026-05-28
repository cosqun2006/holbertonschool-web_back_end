#!/usr/bin/env python3
"""
Async comprehensions module
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehensions() -> List[float]:
    """
    Collects 10 random numbers from async_generator
    using an async comprehension, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
