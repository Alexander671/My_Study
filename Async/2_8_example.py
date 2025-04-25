import asyncio
import time

async def my_coroutine():
    print("Начало")
    asyncio.sleep(1)  # Приостановка на 1 секунду
    print("Конец")

before_coroutine = time.time()
tasks = [my_coroutine() for i in range(5)]

loop = asyncio.get_event_loop()
print("Here we go!")
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

after_coroutine = time.time()

def base_func():
    print("Начало")
    time.sleep(1)  # Приостановка на 1 секунду
    print("Конец")

before_func = time.time()

tasks = [base_func() for i in range(5)]

after_func = time.time()
print(after_coroutine - before_coroutine)
print(time.time() - before_func)