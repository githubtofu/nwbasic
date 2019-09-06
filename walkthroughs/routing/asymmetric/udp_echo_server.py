import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('20.0.0.5', 30000)
#if len(sys.argv) > 1:
#    server_address = ('10.0.0.10', 18000)
sock.bind(server_address)
print('listening on', server_address)

while True:
    data, address = sock.recvfrom(4096)

    print('received', len(data), 'from', address)
    print('data:',data)

    if data:
        sent = sock.sendto(data, address)
        print('sent...')
