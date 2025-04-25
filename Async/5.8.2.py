import asyncio 



async def activate_portal(x): 
    # Функция активации портала. Она должна выводить сообщение о том, что процесс активации начался, ждать x единиц времени, а затем возвращать x * 2.
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2

async def perform_teleportation(x): 
    # Функция, которая выполняет телепортацию. Она должна выводить сообщение о начале процесса телепортации, ждать x единиц времени, а затем возвращать x + 2.
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2

async def recharge_portal(x): 
    # Функция, которая занимается подзарядкой портала. Она должна выводить сообщение о начале процесса подзарядки, ждать x единиц времени, а затем возвращать x * 3.
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 3

async def check_portal_stability(x): 
    # Функция, которая проверяет стабильность портала. Она должна выводить сообщение о начале процесса проверки стабильности, ждать x единиц времени, а затем возвращать x + 4.
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4

async def restore_portal(x): 
    # Функция, которая восстанавливает портал после его использования. Она должна выводить сообщение о начале процесса восстановления, ждать x единиц времени, а затем возвращать x * 5.
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 5

async def close_portal(x): 
    # Функция, которая закрывает портал после использования. Она должна выводить сообщение о начале процесса закрытия, ждать x единиц времени, а затем возвращать x - 1.
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1

async def portal_operator(): 
    activate = await asyncio.ensure_future(activate_portal(2))
    perform  = await asyncio.ensure_future(perform_teleportation(3))
    recharge, check, restore = await asyncio.gather(recharge_portal(4), check_portal_stability(5), restore_portal(6))
    close = await asyncio.ensure_future(close_portal(7))
    print(f"Результат активации портала: {activate} единиц энергии")
    print(f"Результат телепортации: {perform} единиц времени")
    print(f"Результат подзарядки портала: {recharge} единиц энергии")
    print(f"Результат проверки стабильности: {check} единиц времени")
    print(f"Результат восстановления портала: {restore} единиц энергии")
    print(f"Результат закрытия портала: {close} единиц времени")
    
#  Главная  passфункция, которая собирает результаты всех других функций и выводит их. Она должна использовать asyncio.gather() для одновременного запуска всех других функций и затем выводить их 
# результаты.

asyncio.run(portal_operator())