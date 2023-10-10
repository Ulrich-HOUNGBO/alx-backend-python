#!/usr/bin/env python3

"""Write a cororoutine will loup 10 times"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
