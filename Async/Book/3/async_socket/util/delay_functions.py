import asyncio
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


import functools
import time
from contextlib import contextmanager


def duration():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                await func(*args, *kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper