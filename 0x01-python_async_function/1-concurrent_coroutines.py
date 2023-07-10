#!/usr/bin/env python3
"""
Defines an async routine that returns  the list of all the delays
(float values)
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""

    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delays.append(task)

    results = await asyncio.gather(*delays)
    return sorted(results)
