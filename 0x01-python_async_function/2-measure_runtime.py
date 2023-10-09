#!/usr/bin/env python3
"""Measure the runtime of a coroutine"""

import asyncio
import random
from time import perf_counter
from typing import List


async def wait_n(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay seconds and
    then return that number using the asyncio module
    """
    delay_list = []
    for i in range(n):
        delay = random.uniform(0, max_delay)
        delay_list.append(delay)
    start = perf_counter()
    await asyncio.gather(*(asyncio.sleep(i) for i in delay_list))
    end = perf_counter()
    total_time = end - start
    return total_time / n
