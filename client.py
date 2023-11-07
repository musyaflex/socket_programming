import socket

server_ip = input("Enter the server IP: ")
server_port = int(input("Enter the server port: "))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initiate a connection
sock.connect((server_ip, server_port))

while True:
    command = input("Enter command: ")

    sock.sendall(command.encode())


    if command == "POST_STRING":
        messages = []
        while True:
            message = input("enter")
            if message == "&":
                break
            messages.append(message)

        sock.sendall('\n'.join(messages).encode())

    elif command == "POST_FILE":

    elif command == "GET"
        
    elif command == "EXIT":
            break

    else:
        sock.sendall(command.encode())

sock.close()