import asyncio
robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

visits = 0

async def robot_move(name):
    global visits
    print(f'Робот {name} передвигается к месту A')
    visits += 1
    print(f'Робот {name} достиг места A. Место A посещено {visits} раз')
    
async def main():
    tasks = []
    for i, robot_name in enumerate(robot_names):
        tasks.append(asyncio.create_task(robot_move(f"{robot_name}({i})")))

    asyncio.gather(*tasks)

asyncio.run(main())