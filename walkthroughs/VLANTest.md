1. Install [Mininet](http://mininet.org/download/) and [Ryu Controller](https://ryu.readthedocs.io/en/latest/getting_started.html) and vlan and brctl
2. Define Topology
  * see an example at conf directory : [Simple Topology](https://github.com/githubtofu/nwbasic/blob/master/conf/simple_topo.py)
  * add at least three hosts and two switches (for example) to form (host2 - switch1 - host1 - switch2 - host3)
  * save the topology python file as (for example) 'simple.py'
3. Define Switch Operation
  * save the switch code as (for example) 'switch.py'. The code is in the conf directory : [Code](https://github.com/githubtofu/nwbasic/blob/master/conf/learning_sw.py)
4. Run Ryu Controller
  * `ryu-manager ./switch.py ryu.app.ofctl_rest`
5. Run Mininet on a separate terminal
  * `sudo mn --custom ./simple.py --topo mytopo --mac --switch ovsk --controller remote -x`
6. (Optional) On each host, check interfaces with `ifconfig`
7. Clear IP addresses on all interfaces on all hosts. For example, to clear the IP address on h1-eth0 interface,
  * `ip addr flush dev h1-eth0`
8. Add VLAN as needed. For example, to add a VLAN (with ID 100) on h1-eth0 interface,
  * `vconfig add h1-eth0 100`
9. Add bridge as needed. For example,
  * `brctl addbr br0`
  * `brctl addif br0 h1-eth0.100 h1-eth1.100`
10. Set IP addresses on interfaces as needed. For example,
  * `ip addr add 10.0.0.10/24 dev br0`
11. Switch on bridge interfaces. For example,
  * `ip link set dev br0 up`
12. Test connections