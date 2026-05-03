#!/usr/bin/env python3
"""
Asyncio Task yaradan modul.
"""
import asyncio

# wait_random funksiyasını import edirik
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    wait_random funksiyasını götürür və onu bir asyncio Task kimi qaytarır.
    """
    # asyncio.create_task bir coroutine-i icra üçün hazırlayır (schedule)
    return asyncio.create_task(wait_random(max_delay))
