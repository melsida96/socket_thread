import socket
import sys

try:
    s = socket.socket()
except:
    print('Failed to create a socket')
    sys.exit()

print('Socket created')

host = 'localhost'
port = 1551

try:
    s.connect ((host, port))
except:
    print('Connection error')
    sys.exit

message = 'Hello Server'
try:
    s.sendall(message.encode())
except:
    print('Sending error')
    sys.exit()

print('Message send successfully')
reply = s.recv(1024)
print (reply.decode())

s.close()

