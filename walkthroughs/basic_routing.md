## Topology ##
```
h1(10.0.1.1/24) -- (10.0.1.2/24)h2(10.0.2.1/24) -- (10.0.2.2/24)h3(10.0.3.1/24) -- (10.0.3.2/24)h4
```
host 1 and host 3 will be on different networks. host 2 and host 4 will be on different networks. host 2 will be on two networks and can route ip packets between host 1 and host 3. host 3 will be on two network and can route ip packets between host 2 and host 4. To route packets from host 1 to host 4, proper routing paths should be set up on host 2 and host 3.

use this [topology file](../conf/simple_routing_mini.py)

## Basic Steps ##

Run mininet : `sudo mn --custom ./basic_routing_mini.py --topo mytopo --mac --switch ovsk --controller remote -x`

Remove IPs on all hosts. For example `ip addr flush dev <<Interface name on host 1>>` for Host 1

Set IPs on hosts.
* Host 1 : `ip addr add 10.0.1.1/24 dev <<Interface name on host 1>>`
* Host 2 IPs : 10.0.1.2/24 for the interface connected to Host 1. 10.0.2.1 for the interface connected to Host 3.
* Host 3 IP: 10.0.2.1/24

Try ping from Host 1 to Host 2

Try ping from Host 1 to Host 3

Turn on routing on host 2 and host 3 : `sysctl -w net.ipv4.ip_forward=1`

Add default gateway on host 1 and 4. For example, `route add default gw 10.0.1.2` for host 1.

Try ping from Host 1 to Host 2

Try ping from Host 1 to Host 3

Try ping from Host 1 to Host 4

Add routes on host 2 and host 3 : For example, `route add -net 10.0.3.0 netmask 255.255.255.0 gw 10.0.2.2` for Host 2

Try ping from Host 1 to Host 4


