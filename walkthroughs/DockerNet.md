## Run Containers
 * `$ docker run -t --network none -i --name container1 ubuntu /bin/bash`
 * `$ docker run -t --network none -i --name container2 ubuntu /bin/bash`

## Create switch bridge and create ports
* `$ ovs-vsctl add-br ovs-br1`
* `$ ifconfig ovs-br1 173.16.1.1 netmask 255.255.255.0 up`
* `$ ovs-docker add-port ovs-br1 eth1 container1 --ipaddress=173.16.1.2/24 --gateway=173.16.1.1`
* `$ ovs-docker add-port ovs-br1 eth1 container2 --ipaddress=173.16.1.3/24 --gateway=173.16.1.1`

## (add external port)
* `ovs-vsctl add-port ovs-br1 eth0`

## Provider / Subscriber Test

## Analyzer Test

## controller setting
* `ovs-appctl bridge/dump-flows ovs-br1`
* `ovs-ofctl dump-ports-desc ovs-br1`
* `ovs-ofctl add-flow ovs-br1 in_port=2,actions=1,LOCAL`

## some n/w setups
* `ip route del default`
* `ip route add default gw 192.168.11.1` OR `ip route add default via 192.168.11.1 dev eth1` (https://serverfault.com/questions/123553/how-to-set-the-preferred-network-interface-in-linux)
* `ip link del docker0`
* `ovs-vsctl del-br ovs-br1`
* `ifconfig eno1 down` && `dhclient eno1`

## (install ping)
* `docker exec -it container1 apt-get install iputils-ping`

## (run without sudo)
* `sudo groupadd docker`
* `sudo gpasswd -a $USER docker`
* `newgrp docker`
* `docker run hello-world`

## (run sudo with passwords)
* `echo <password> | sudo -S <command>`

## rate limiting
* http://docs.openvswitch.org/en/latest/howto/qos/

===

## VLAN & Aliasing
* [Simple Walkthrough](walkthroughs/VLANTest.md)
* Host Network Interfaces
* Switching
* 802.1Q packet

* `sudo apt-get install vlan`
* `sudo apt-get install bridge-utils`
* `sudo apt-get install xterm`
