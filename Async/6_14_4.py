import random
import asyncio

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")

async def main():
    configs = [(shape, color, action) for shape in shapes for color in colors for action in actions]

    for config in configs:
        asyncio.create_task(launch_firework(*config))
    try:
        await asyncio.sleep(6)
    except asyncio.CancelledError:
        pass
asyncio.run(main())
