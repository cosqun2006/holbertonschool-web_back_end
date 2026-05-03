#!/usr/bin/env python3
"""
İcra vaxtını ölçən modul.
"""
import time
import asyncio

# wait_n funksiyasını import edirik
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    wait_n funksiyasının icra vaxtını ölçür və orta vaxtı qaytarır.
    """
    start_time = time.perf_counter()

    # Asinxron funksiyanı sinxron funksiya daxilində işə salırıq
    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
