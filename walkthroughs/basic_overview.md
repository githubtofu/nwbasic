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
10.0.0.1 ~ 10.0.0.255 because of the network prefix '24'.

Let's set an IP address on host 2 using `ip addr add 10.0.0.2/24 dev <<Interface name on host 2>>`

Try ping from host 1 using `ping 10.0.0.2`

Now ping succeeds. First, ARP request is sent from host 1 by broadcast as before, but this time, a response is sent from host 2
to host 1 since host 2 now has IP address and has to respond to ARP request for that IP address. 


