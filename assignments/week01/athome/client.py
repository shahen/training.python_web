import socket

client = socket.socket()
client.connect(('localhost', 6060))

client.sendall('5,5')
data = client.recv(4096)
print data

client.close()
