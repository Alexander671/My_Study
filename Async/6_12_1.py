codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


import asyncio
import functools

                        

async def print_message(message):
    await asyncio.sleep(1)
    print(f"Сообщение: {message}")

def print_code(code, _):
    print(f"Код: {code}")

async def main():
    for message, code in zip(messages, codes):
        task = asyncio.create_task(print_message(message))
        task.add_done_callback(functools.partial(print_code, code))
        await task

asyncio.run(main())