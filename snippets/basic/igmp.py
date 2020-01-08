import socket
import struct
import select
import sys

#MCAST_GRP = '239.1.2.101'
MCAST_GRP = sys.argv[1]
MCAST_PORT = 5007
IS_ALL_GROUPS = True
server_address = (MCAST_GRP, 10000)
ui_port = 22222

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setblocking(0)
#sock.bind(server_address)

mreq = struct.pack("4sL", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    asock = select.select([sock],[],[]) 
    dd, aa = sock.recvfrom(100)
    print("Got Something", MCAST_GRP, dd)
    if dd == "CLOSE":
        print("closing...")
        break

    sock.sendto('RX_M ' + MCAST_GRP, ('127.0.0.1', ui_port))
