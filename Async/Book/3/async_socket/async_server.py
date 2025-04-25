import socket
import signal

import asyncio
from asyncio import AbstractEventLoop

import logging

from util.delay_functions import delay

async def echo(connection, address, loop:AbstractEventLoop):
    while data := await loop.sock_recv(connection, 1024): 
        try:
            if data == b'boom\r\n':
                raise Exception('Неожиданная ошибка сети')
            print(f'Получены данные: {data}. От следующего клиента: {address}.')
            await loop.sock_sendall(connection, data)
        except Exception as e:
            logging.exception(e)

echo_tasks = []

async def listen_for_connection(server_socket, loop:AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        task = asyncio.create_task(echo(connection, address, loop))
        echo_tasks.append(task)

class GracefulExit(SystemExit):
    pass

def shutdown():
    raise GracefulExit()

async def close_echo_tasks(echo_tasks):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass
            


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    loop = asyncio.get_event_loop()    
    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await listen_for_connection(server_socket, loop)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()