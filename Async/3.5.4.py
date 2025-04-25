import asyncio

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter_with_pause(label):
    while max_counts[label] > counters[label]:
        counters[label] += 1
        await asyncio.sleep(delays[label])
        print(f"{label}: {counters[label]}")
    


async def main():
    task1 = asyncio.create_task(counter_with_pause("Counter 1"))
    task2 = asyncio.create_task(counter_with_pause("Counter 2"))
    task3 = asyncio.create_task(counter_with_pause("Counter 3"))
    await task1
    await task2 
    await task3

asyncio.run(main())