import socket

s = socket.socket()
port = 5235
s.bind(('localhost', port))
s.listen(1)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you for your connecting')
    c.close()
