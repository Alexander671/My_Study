import asyncio

async def test():
    pass

async def main():
    task = asyncio.create_task(test())
    print(task.get_name())  # Task-2


asyncio.run(main())
