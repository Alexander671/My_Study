import socket

target_host = "127.0.0.2"
target_port = 9998

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

# send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# recieve some data
response = client.recv(4096)

print(response.decode())
client.close()