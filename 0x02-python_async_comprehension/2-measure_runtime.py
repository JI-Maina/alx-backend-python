#!/usr/bin/env python3
"""
Defines a coroutine that will execute async_comprehension four times in
parallel and measure the total runtime and return it
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measures the total runtime of async_comprehension and returns it"""

    start = time.time()

    tasks = []
    for _ in range(4):
        task = async_comprehension()
        tasks.append(task)

    result = await asyncio.gather(*tasks)

    end = time.time()

    time_taken = end - start

    return time_taken
