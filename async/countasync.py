#!/usr/bin/env python3

import asyncio

async def count(n):
    print(f"One {n}")
    await asyncio.sleep(1) # I/O mocking
    print(f"Two {n}")


async def main():
    # Calls 'count' func then pauses 3 times, immediately
    await asyncio.gather(count(1), count(2), count(3))
    # Entire call takes 1 second. Sequential execution would take 3 seconds

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
