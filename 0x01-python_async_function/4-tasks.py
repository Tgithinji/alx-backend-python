#!/usr/bin/env python3
"""
4-tasks module
"""
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times
    """
    delays_list = []
    sorted_list = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delays_list.append(task)

    for task in asyncio.as_completed(delays_list):
        delay = await task
        sorted_list.append(delay)

    return sorted_list
