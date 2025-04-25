import asyncio

async def generate(lst):
    for i in lst:
        print("Корутина generate с аргументом", i)


async def main():
    await generate(range(0, 10))

asyncio.run(main())