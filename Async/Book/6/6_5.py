import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List
import time

def countdown(count_from: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_from:
        counter = counter + 1
    end = time.time()
    print(f'Finished counting to {count_from} in {end - start}')
    return counter

async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [100000000, 1, 3, 5, 22]
        calls: List[partial[int]] = [partial(countdown, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))

        results = await asyncio.gather(*call_coros)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())