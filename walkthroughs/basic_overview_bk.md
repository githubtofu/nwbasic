see [Basic Setup](basic_setting.md)

## Basic topology ##

```
Host 1 -- Switch -- Host 2
            |
          Host 3
```

## How packets are sent on LAN ##

For communication over Ethernet, hosts need IP addresses and MAC addresses.
Check the interface name (other than local loop back interface) and addresses of a host with `ifconfig`
* Host 1's Interface name :
* Host 1's IP address :
* Host 1's MAC address :
* Host 2's Interface name :
* Host 2's IP address :
* Host 2's MAC address :

(Learn about IP address and MAC address using wikipedia)

Let's remove IP addresses using `ip addr flush dev <<Interface name>>` on all the hosts.

Try ping from host 1 to host 2 using a random IP address.

Network is unreachable since there is no interface to send the ping packet.

Let's set an IP adress on host 1 using `ip addr add 10.0.0.1/24 dev <<Interface name on host 1>>`

Try ping from host 1 using `ping 10.0.0.2`

Now we have an interface to send out but to send an Ethernet packet to Host 2, Host 1 should know Host 2's IP address and MAC address.
If we ping to 10.0.0.2, host 1 try to figure out MAC address attached to the IP address 10.0.0.2 by sending out ARP requests using broadcast.
Note (on wireshark) that ARP packets are sent from host 1 to all other hosts since the destination MAC address of the ARP packets are the broadcast address.
But there are no hosts with that IP address resulting in no response to the ARP requests.
Since the MAC address is unknown, we can't send out ping packet and we get 'Destination Host Unreachable' error.

Stop ping by pressing Control-C

Try ping from host 1 using `ping 10.0.1.0`

This time we get 'Network unreachable` error instead of 'Host unreachable` since 10.0.1.0 is on a different network.
This is because we set the IP address using 10.0.0.1/24 and the interface can send packet directly only to IP addresses in the range
10.0.0.1 ~ 10.0.0.255 because the network prefix length is 24. (Learn about network prefix length https://datapath.io/resources/blog/what-are-network-prefixes/ and subnet mask)

Let's set an IP address on host 2 using `ip addr add 10.0.0.2/24 dev <<Interface name on host 2>>`

Try ping from host 1 using `ping 10.0.0.2`

Now ping succeeds. First, ARP request is sent from host 1 by broadcast as before, but this time, a response is sent from host 2
to host 1 since host 2 now has IP address and has to respond to ARP request for that IP address. 


## Communication with a remote host ##

Exit mininet using `exit`

Start mininet using `sudo mn --topo single,3 --mac --controller remote --switch ovsk -x --nat`

Run wireshark on host 1

Try ping from host 1 using `ping www.airplug.com`

(If dns is not working add dns server using [Adding DNS server](add_dns.md))

Check packets on wireshark. Remember that host 1 can't send a packet directlry to a remote host.
It can only send a packet to a host in its own network (10.0.0.1 ~ 10.0.0.255). The packet is sent to www.airplug.com using the following steps.

(host 1 needs to know the IP address corresponding to www.airplug.com. It sends out DNS queries to the DNS server (for example, 8.8.4.4) but it can't send the query directlry to 8.8.4.4 since it is on a remote network. It should send the query to a host on its own network which is connected to the Internet via another interface. In our case that host is NAT.)

1. host 1 sends ARP queries for 10.0.0.4 (NAT) and gets a response saying the MAC address of 10.0.0.4 is 00:00:00:00:00:04

2. host 1 sends DNS query destined to 8.8.4.4 to 00:00:00:00:00:04(NAT)

3. the DNS query is sent outward via NAT

4. the DNS response from 8.8.4.4 is routed to 10.0.0.1 (host 1) via NAT

5. host 1 sends ping destined to IP address of www.airplug.com to NAT

6. ping is sent outward by NAT

7. ping response is routed to 10.0.0.1 (host 1) via NAT

Check ARP, DNS, ICMP packets on wireshark.

## UDP send/receive ##

Run mininet as before

Send UDP packets using [client program](../snippets/basic/udp_echo_client.py) on host 1 and [server program](../snippets/basic/udp_echo_server.py) on host 2

Check packets on wireshark

Send UDP packets from host 1 to an unused port and check ICMP messages on wireshark

## TCP send ##

Send a TCP packet from host 1 using [client program](../snippets/basic/tcp_client.py)

Note syn packet on wireshark

Run a TCP server on host 2 using [server program](../snippets/basic/tcp_server.py) and send a TCP packet from host 1 to host 2

Note 3-way handshake on wireshark

Examine the TCP packet containing the message on wireshark

Check what packets are exchanged when the socket is closed.
