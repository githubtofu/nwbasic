## Run Containers
 * `$ docker run -t -i --name container1 ubuntu /bin/bash`
 * `$ docker run -t -i --name container2 ubuntu /bin/bash`

## Create switch bridge and create ports
* `$ ovs-vsctl add-br ovs-br1`
* `$ ifconfig ovs-br1 173.16.1.1 netmask 255.255.255.0 up`
* `$ ovs-docker add-port ovs-br1 eth1 container1 --ipaddress=173.16.1.2/24`
* `$ ovs-docker add-port ovs-br1 eth1 container2 --ipaddress=173.16.1.3/24`

## Provider / Subscriber Test

## Analyzer Test


===

## VLAN & Aliasing
* [Simple Walkthrough](walkthroughs/VLANTest.md)
* Host Network Interfaces
* Switching
* 802.1Q packet

* `sudo apt-get install vlan`
* `sudo apt-get install bridge-utils`
* `sudo apt-get install xterm`
