import asyncio
from util.delay_functions import delay

async def main():
    task_delay_10 = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task_delay_10), timeout=5)
        print(result)
    
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task_delay_10
        print(result)

asyncio.run(main())