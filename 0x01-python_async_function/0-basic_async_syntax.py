#!/usr/bin/env python3
"""
inititiation to async asyncio and await python
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
     max delay is a the max delai
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
