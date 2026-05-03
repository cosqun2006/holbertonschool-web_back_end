#!/usr/bin/env python3
"""
Asinxron coroutine modulu.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    0 və max_delay arasında təsadüfi bir müddət gözləyir
    və həmin müddəti qaytarır.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
