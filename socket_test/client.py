import socket

s = socket.socket()
port = 5235
s.connect(('localhost', port))
print s.recv(1024)
s.close()
