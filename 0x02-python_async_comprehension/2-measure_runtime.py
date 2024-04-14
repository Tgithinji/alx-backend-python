#!/usr/bin/env python3
"""2-measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time: float = time.time()
    await asyncio.gather(
       async_comprehension(),
       async_comprehension(),
       async_comprehension(),
       async_comprehension()
    )
    end_time: float = time.time()
    runtime: float = end_time - start_time
    return runtime
