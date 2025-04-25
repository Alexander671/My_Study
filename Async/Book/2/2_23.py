import asyncio      
from util.delay_functions import duration

@duration()
async def cpu_bound_work():
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter

@duration()
async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 6
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one
    
asyncio.run(main(), debug=True)