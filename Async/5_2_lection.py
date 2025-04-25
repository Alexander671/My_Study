import asyncio

async def coroutine_1():
    await asyncio.sleep(1)
    print("Корутина 1 выполнена")

async def coroutine_2():
    await asyncio.sleep(2)
    print("Корутина 2 выполнена")

async def main():
    # Создаем задачи из корутин
    await coroutine_1()
    await coroutine_2()
    print("Все корутины выполнены")

import time
before = time.time()
# Точка входа программы
asyncio.run(main())

print(time.time() - before)