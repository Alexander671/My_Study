
codes = ["56FF4D", "A3D2F7", "B1C948", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]


messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]
import asyncio
import functools

async def main_coro():
    pass
              

def print_message(message, _):
    print(f"Сообщение: {message}")

def print_code(code, _):
    print(f"Код: {code}")

async def main():
    for message, code in zip(messages, codes):
        task = asyncio.create_task(main_coro())

        try:
            assert (int(code[-1])) % 2 == 0
            task.add_done_callback(functools.partial(print_message,  'Неверный код, сообщение скрыто'))

        except:
            task.add_done_callback(functools.partial(print_message, message))

        task.add_done_callback(functools.partial(print_code, code))        
        await task
 
asyncio.run(main())