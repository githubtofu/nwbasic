## Walkthrough ##
1. Install Mininet, Ryu Controller, VLAN and Bridge contol as needed. Installing packages is the easiest way.
  *  [Mininet](http://mininet.org/download/)
  *  [Ryu Controller](https://ryu.readthedocs.io/en/latest/getting_started.html)
  * `sudo apt-get install vlan`
  * `sudo apt-get install bridge-utils`
2. Define Topology
  * see an example at conf directory : [Simple Topology](https://github.com/githubtofu/nwbasic/blob/master/conf/simple_topo.py)
  * add at least three hosts and two switches (for example) to form (host2 - switch1 - host1 - switch2 - host3)
  * save the topology python file as (for example) 'simple.py'
3. Define Switch Operation (Learning switch in this example)
  * save the switch code as (for example) 'switch.py'. The code is in the conf directory : [Code](https://github.com/githubtofu/nwbasic/blob/master/conf/learning_sw.py)
4. Run Ryu Controller
  * `ryu-manager ./switch.py ryu.app.ofctl_rest`
5. Run Mininet on a separate terminal
  * `sudo mn --custom ./simple.py --topo mytopo --mac --switch ovsk --controller remote -x`
6. (Optional) On each host, check interfaces with `ifconfig`
7. Clear IP addresses on all interfaces on all hosts. For example, to clear the IP address on h1-eth0 interface,
  * `ip addr flush dev h1-eth0`
8. Add VLANs as needed. For example, to add a VLAN (with ID 100) on h1-eth0 interface,
  * `vconfig add h1-eth0 100`
9. Add bridges as needed. Add interfaces to created bridges as needed. For example,
  * `brctl addbr br0`
  * `brctl addif br0 h1-eth0.100 h1-eth1.100`
10. Set IP addresses on interfaces as needed. For example,
  * `ip addr add 10.0.0.10/24 dev br0`
  * A recommended setting is at the bottom of this file
11. Switch on bridge and vlan interfaces. For example,
  * `ip link set dev br0 up`
12. (Optional) Run wireshark on background on each host.
13. Test connections

## Recommended Setting ##
### physical ###
* host2 - switch1 - host1 - switch2 - host3
### VLANs ###
* host2 - (VLAN 100) - host1 - (VLAN 100, 101) - host3
### Bridge Interface ###
* host1 : br0 bridging h1-eth0.100 and h1-eth1.100
### IPs ###
* host2 : 10.0.0.12/24 on h2-eth0.100
* host1 : 10.0.0.10/24 on br0, 10.0.1.10/24 on h1-eth1.101
* host3 : 10.0.0.13/24 on h3-eth0.100, 10.0.1.13/24 on h3-eth0.101
