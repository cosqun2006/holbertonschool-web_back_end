#!/usr/bin/env python3
"""
Eyni vaxtda bir neçə coroutine icra edən modul.
"""
import asyncio
from typing import List

# Əvvəlki tapşırıqdan wait_random-u import edirik
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_random funksiyasını n dəfə işə salır və nəticələri
    bitmə ardıcıllığına görə siyahı şəklində qaytarır.
    """
    delays = []
    tasks = []

    # n qədər task yaradırıq
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    # asyncio.as_completed istifadə edirik ki, bitən kimi siyahıya əlavə edək
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
