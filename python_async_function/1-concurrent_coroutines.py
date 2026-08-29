#!/usr/bin/env python3
"""Run multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the delays in ascending order."""
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    delays = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
