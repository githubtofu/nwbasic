import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_addr = ('10.0.0.10', 18000)
server_addr = ('20.0.0.5', 30000)
#if len(sys.argv) > 1:
#    my_addr = ('20.0.0.5', 30000)
#    server_addr = ('10.0.0.10', 18000)
sock.bind(my_addr)

message = 'Test message............'

try:
    for i in range(1000):
        print('sending msge')
        sent = sock.sendto(message, server_addr)
        data, server = sock.recvfrom(4096)
        print('received',data)
        time.sleep(2)

finally:
    print('closing....')
    sock.close()
