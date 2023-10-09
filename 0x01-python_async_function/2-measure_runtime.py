#!/usr/bin/env python3
"""Measure the runtime of a coroutine"""

import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay seconds and
    then return that number using the asyncio module
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
