import asyncio 

async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2

async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2

async def portal_operator():
    future_activate = asyncio.ensure_future(activate_portal(2))
    result_activate = await future_activate
    if result_activate > 4:
        result_activate = 1
    future_teleport = asyncio.ensure_future(perform_teleportation(result_activate))
    result_teleport = await future_teleport
    
    print(f"Результат активации портала: {result_activate} единиц энергии")
    print(f"Результат телепортации: {result_teleport} единиц времени")

import time

before = time.time()
asyncio.run(portal_operator())
print(time.time() - before)