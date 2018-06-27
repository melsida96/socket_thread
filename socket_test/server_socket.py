import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind (('localhost', 19999))
server.listen(1)
conn, address = server.accept()

while True:
    data = conn.recv(1024)
    print data
    if not data:
        break
    conn.sendall('I have received your message')
conn.close()
