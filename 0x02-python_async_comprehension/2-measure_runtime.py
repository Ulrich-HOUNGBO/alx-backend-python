#!/usr/bin/env python3

"""mesure runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
     Run time for four parallel comprehensions
    """
    task = []
    start_time = time.time()
    for i in range(4):
        task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*task)
    end_time = time.time()
    return end_time - start_time
