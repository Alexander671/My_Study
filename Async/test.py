import asyncio

async def arange(x):
    for i in range(x):
        yield i
    
async def main():
    async for i in arange(5):
        await asyncio.sleep(1) 
        print(i)

asyncio.run(main())