#!/usr/bin/env python3
"""wait_random module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
