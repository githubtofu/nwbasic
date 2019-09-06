import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('20.0.0.5', 10000)
print('starting up on ...')
sock.bind(server_addr)

sock.listen(1)

while True:
    print('waiting...')
    connection, client_addr = sock.accept()

    try:
        print('connection from ', client_addr)

        while True:
            data = connection.recv(16)
            print('received ',data)
            if data:
                print('sending data back')
                connection.sendall(data)
            else:
                print('no more data')
                break
    finally:
        connection.close()
