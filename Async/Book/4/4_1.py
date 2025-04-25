import asyncio
import socket
from types import TracebackType
from typing import Optional, Type

class ConnectionSocket:
    def __init__(self, server_socket) -> None:
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        print('Вход в контекстный менеджер, ожидание подключения...')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print(f'Подключение подтверждено')
        return self._connection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'Выход из контекстного менеджера')
        self._connection.close()
        print(f'Подключение закрыто')

async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.setblocking(False)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen()

    async with ConnectionSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)

asyncio.run(main())
