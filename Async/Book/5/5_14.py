import asyncio
from util.delay_functions import delay, duration
async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer

@duration()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число {number}')
asyncio.run(main())