import asyncio
from util.delay_functions import duration, delay


@duration()
async def cpu_bound_work():
    counter = 0
    for i in range(10000000):
        counter += 1
    return counter

@duration()
async def main():
    delay_task = asyncio.create_task(delay(4))
    await delay_task

    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    await task_one
    await task_two

asyncio.run(main())
    