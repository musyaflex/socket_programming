import socket

server_ip = "127.0.0.1"
server_port = 16011


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initiate a connection
sock.connect((server_ip, server_port))