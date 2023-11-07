import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    print("========================== Initialize socket ==========================")
    server_ip = input("input IP address: ")
    server_port = int(input("input port number: "))
    try:
        sock.connect((server_ip, server_port))
        break

    except ConnectionRefusedError:
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
            if line == "&":
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
        sock.sendall(command.encode())

sock.close()