import socket
import sys
import threading

host = 'localhost'
port = 1551
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed create socket')

try:
    s.bind(('localhost', port))
except:
    print('Binding failed')

s.listen(5)

print('Socket is ready')

def client_thread(conn):
    welcome ="Welcome to server.\n Write a message: "
    conn.send(welcome.encode())
    while 1:
        data = conn.recv(1024)
        reply = data.decode()
        if not data:
            break
        print(reply)
        conn.sendall(reply.encode())
    conn.close()


while 1:

    conn, addr = s.accept()
    print('Connected with' + addr[0] + ':' + str(addr[1]))
    start_new_thread(client_thread, (conn,))

s.close()
