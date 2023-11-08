import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    print("========================== Initialize socket ==========================")
    server_ip = input("input IP address: ")
    server_port = 0
    server_port_input = input("input port number: ")
    if not server_port_input.isdigit():
        print("Error: connection is not built, try again")
        continue
    try:
        server_port = int(server_port_input)
        sock.connect((server_ip, server_port))
        msg_str = "connection test"
        sock.sendall(msg_str.encode())
        break

    except socket.error as e:
        print("Error: connection is not built, try again")


while True:
    print("============================ Input command ============================")
    command = input("Input command: ")

    sock.sendall(command.encode())

    if command == "POST_STRING":
        print("=============== Content (Type a lone '&' to end message) ===============")
        message = "POST_STRING"
        count = 0
        while True:
            line = input('client:')
            if line == "":
                print("client: the input cannot be empty.")
                continue
            if line == "&":
                count = count + 1
                print('server: OK')
                print('---')
                print('Sent {} messages to (IP address:{}, port number:{})'.format(count, server_ip, server_port))
                print('Connect status: OK')
                print('Send status: OK')
                print('---')
                sock.sendall(line.encode())
                break
            count = count + 1
            message += line + "\n"
            sock.sendall(line.encode())

    elif command == "POST_FILE":
        print("ok")
    elif command == "GET":
        print("ok")
    elif command == "EXIT":
        break
    else:
        print("server: ERROR - Command not understood")

sock.close()