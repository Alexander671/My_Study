import asyncio

async def coro_n(msg):
    await asyncio.sleep(1)
    print(f"Coroutine {msg} is done")


async def main():
    for i in range(1, 4):
        await coro_n(i)

asyncio.run(main())