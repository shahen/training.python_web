import socket
import sys

# Create a TCP/IP socket
server = socket.socket()
# Bind the socket to the port
server_address = ('localhost', 50000)

server.bind((server_address))
# Listen for incoming connections
server.listen(5)

while True:
    # Wait for a connection
    conn, addr = server.accept()

    try:
        # Receive the data and send it back
	msg = conn.recv(4906)
	conn.sendall(msg)
        

    finally:
        # Clean up the connection
	server.close()
