#!/usr/bin/env python3
"""
Task-lar vasitəsilə eyni vaxtda icra modulunu yeniləmək.
"""
import asyncio
from typing import List

# Gərəkli funksiyaları import edirik
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random istifadə edərək n dəfə wait_random-u icra edir.
    """
    delays = []
    tasks = []

    # n qədər Task yaradırıq
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # Bitmə ardıcıllığına görə siyahıya əlavə edirik
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
