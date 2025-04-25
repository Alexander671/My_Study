import asyncio
from random import randint


async def background_timer(n: int):
    print(f'Timer {n} started')
    i = 1
    while i <= n:
        print(f'Прошел {i} тик')
        await asyncio.sleep(1)
        i += 1
    print(f'Timer {n} stopped')
    return 1


async def async_gen(n):
    for i in range(n):
        await asyncio.sleep(randint(1, n))
        yield i


async def main(n: int) -> None:
    task = asyncio.create_task(background_timer(7))
    async for i in async_gen(n):
        print(f'Iterator part {i}')
    await task


if __name__ == '__main__':
    asyncio.run(main(3))