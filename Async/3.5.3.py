import asyncio

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

async def counter_with_pause(label, sec):
    while max_counts[label] > counters[label]:
        counters[label] += 1
        await asyncio.sleep(sec)
        print(f"{label}: {counters[label]}")


async def main():
    task1 = asyncio.create_task(counter_with_pause("Counter 1", 1))
    task2 = asyncio.create_task(counter_with_pause("Counter 2", 1))
    await task1
    await task2 


asyncio.run(main())