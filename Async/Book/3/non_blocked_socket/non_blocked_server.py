# эта версия работает намного лучше
# потому что используется не блокирующий сокет
# а также мы используем систему уведомлений OS

import socket
import selectors

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # тип адреса, протокол TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # переиспользовать порт

server_socket.bind(('127.0.0.1', 8000))

server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events = selector.select(timeout=5)
    if len(events) == 0:
        print('Событий нет, подожди ещё!')

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {client_address}!')
            selector.register(connection, selectors.EVENT_READ)

        else:
            data = event_socket.recv(1024)
            print(f'Получены данные: {data}')
            event_socket.send(data)