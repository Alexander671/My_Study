# эта версия синхрона
# потому что сокеты блокирующие
# а также эта версия тратит очень много ресурсов
# потому что мы постоянно опрашиваем сокет
# проверям пришли ли результаты
# список connections растет

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # тип адреса, протокол TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # переиспользовать порт
server_socket.bind(('127.0.0.1', 8000))

server_socket.listen()
connections = []
connection, client_address = server_socket.accept()

try:
    while True:
        print(f'Получен запрос на подключение от {client_address}!')
        connections.append(connection)
        print(connections)
        for connection in connections:
            buffer = b''
            while buffer [-2:] != b'\r\n':
                data = connection.recv(256)
                if not data or data == b'STOP':
                    break
                else:
                    print(f'Получены данные: {data}!')
                    buffer = buffer + data
            print(f'Все данные: {buffer}')
            connection.send(buffer)
finally:
    server_socket.close()