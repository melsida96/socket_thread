import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect (('localhost', 19999))
client.sendall ('Message from client')
data = client.recv(1024)
client.close()
print repr(data)

