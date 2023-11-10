import os
import socket
import struct

BUFFER_SIZE = 4096


def send_file(sock, file_path):
    # Get the file size
    try:
        file_size = os.path.getsize(file_path)
    except FileNotFoundError:  # Error handling when file do not exist
        print(f'Cannot find the file')
        error_msg = "close"
        sock.sendall(error_msg.encode())
        print(sock.recv(BUFFER_SIZE).decode())
        return
    except OSError:
        print(f'Cannot find the file')
        error_msg = "close"
        sock.sendall(error_msg.encode())
        print(sock.recv(BUFFER_SIZE).decode())
        return
 
    if file_size > 256:
        print(f'File size should be no more than 256 bytes')
        error_msg = "close"
        sock.sendall(error_msg.encode())
        sock.recv(BUFFER_SIZE).decode()
        return
 
    print(f'Transfer file absolute path: {file_path}')
 
    # Truncate or pad the file name to a maximum length of 128 bytes
    file_name = os.path.basename(file_path)[:128].encode('utf-8')
 
    # Pack the file information
    file_size_data = struct.pack('128sl', file_name, file_size)
 
    # Send the file information to the server
    sock.sendall(file_size_data)
 
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            sock.sendall(data)
 
    # Wait for the server to acknowledge the file information
    response = sock.recv(BUFFER_SIZE).decode()
    print(response)


while True:
    print("========================== Initialize socket ==========================")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialize socket
    sock.settimeout(5)  # 5 seconds timer for error handling
    server_ip = input("input IP address: ")
    server_port = 0
    server_port_input = input("input port number: ")
    if (not server_port_input.isdigit()) or (int(server_port_input) > 65535):  # Error handling of incorrect port
        print("Error: connection is not built, try again")
        continue
    try:
        server_port = int(server_port_input)
        sock.connect((server_ip, server_port))  # Connect to server
        msg_str = "connection test"
        sock.sendall(msg_str.encode())  # Send test message
        sock.recv(BUFFER_SIZE).decode()
        if server_ip == "localhost":
            server_ip = "127.0.0.1"
        break
    except socket.timeout:
        print("Error: cannot send test message to server, try again")  # If after 5 seconds test message not received
    except socket.error:
        print("Error: connection is not built, try again")  # Error handling of incorrect ip-port combination
 
first_command = True
while True:
    if first_command:
        print("============================ Input command ============================")
        first_command = False
    else:
        print("==============================next command=============================")
    command = input("Input command: ")
    
    if command == "POST_STRING":
        sock.sendall(command.encode())  # Send POST_STRING to server
        print("=============== Content (Type a lone '&' to end message) ===============")
        count = 0  # Counter for outputting total number of messages
        while True:
            line = input('client:')
            if line == "":
                print("client: the input cannot be empty.")  # Error handling for empty string
                continue
            if line == "&":
                sock.sendall(line.encode())
                count += 1
                ack = sock.recv(BUFFER_SIZE).decode()  # Receive acknowledgement from server
                break
            count += 1
            sock.sendall(line.encode())
        if ack == 'server: OK':  # ACK received
            print(ack)
            print('---')
            print('Sent {} messages to (IP address:{}, port number:{})'.format(count, server_ip, server_port))
            print('Connect status: OK')
            print('Send status: OK')
            print('---')
        else:  # Error printed
            print('---')
            print("Connect status: ERROR")
            print("Send status: ERROR")
            print('---')
    elif command == "POST_FILE":
        sock.sendall(command.encode())
        print(sock.recv(BUFFER_SIZE).decode())
        file_path = input('client: ')
 
        # Send the file to the server
        send_file(sock, file_path)
    elif command == "GET":
        sock.sendall(command.encode())
        print("---Received Messages---")
        in_post = True
        message = []
        while in_post:
            rcv_msg = sock.recv(BUFFER_SIZE).decode()
            post_msg_str = rcv_msg.replace("server", "client")  #
 
            if post_msg_str == "client: &":
                message.append(post_msg_str)
                in_post = False
            else:
                message.append(post_msg_str)
 
        for msg in message:
            print(msg)
        print('(IP address: {}, port number:{})'.format(server_ip, server_port))
        print("Connect status: OK")
        print("Send status: OK")
 
 
    elif command == "EXIT":
        sock.sendall(command.encode())
        ok_msg = sock.recv(BUFFER_SIZE).decode()
        print(ok_msg)
        sock.close()
        break
    else:
        sock.sendall(command.encode())
        error_msg = sock.recv(BUFFER_SIZE).decode()
        print(error_msg)
 
sock.close()