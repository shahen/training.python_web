#!/bin/env python
import socket
import re
server = socket.socket()
server.bind(('localhost', 6060))
server.listen(2)

while True:
	conn, addr = server.accept()
	try:
		a,b = re.split(',',conn.recv(4096))
		sum = int(a) + int(b)
		conn.sendall(str(sum))
	finally:
		server.close()
