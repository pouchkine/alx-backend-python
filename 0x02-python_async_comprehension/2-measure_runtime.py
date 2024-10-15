#!/usr/bin/env python3
"""
end project list comprehension asynchone
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    return flaot
    """
    s = perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    s = perf_counter() - s
    return s
