#!/usr/bin/env python3
"""0-async_generator module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times then yields a random number between 0 to 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
