import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('20.0.0.5', 10000)
my_addr = ('10.0.0.10', 20076)
#if len(sys.argv) > 1:
#    my_addr = ('20.0.0.10', 20018)
sock.bind(my_addr)
print('connecting to ....', server_address)
sock.connect(server_address)
print('connected')

try:
    msg = 'This is a message that should be echoed'
    print('sending', msg)
    sock.sendall(msg)

    amount_received = 0
    amount_expected = len(msg)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received', data)

finally:
    print('closing socket')
    sock.close()
