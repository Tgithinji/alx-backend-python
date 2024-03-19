#!/usr/bin/env python3
"""
1-concurrent_coroutine module
"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times
    """
    delays_list = []
    sorted_list = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delays_list.append(task)

    for task in asyncio.as_completed(delays_list):
        delay = await task
        sorted_list.append(delay)

    return sorted_list
