#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written and"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds and
    eventually returns it."""
    delays: List[float] = []
    all_list: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        result = await delay
        all_list.append(result)
    return all_list
