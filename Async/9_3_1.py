import asyncio

ips = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

event = asyncio.Event()

async def camera(name):
    print(f'Датчик {name} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {name} активирован, "Wee-wee-wee-wee"')
    
async def set_event():
    
    # Выводим сообщение о начале установки события
    print('Датчики зафиксировали движение')
    
    # Устанавливаем событие
    event.set()

async def main():
    tasks = []
    for i, ip in enumerate(ips):
        tasks.append(asyncio.create_task(camera(f'{i} IP-адрес {ip}')))

    task_event = asyncio.create_task(set_event())
    await asyncio.gather(*tasks, task_event)

asyncio.run(main())