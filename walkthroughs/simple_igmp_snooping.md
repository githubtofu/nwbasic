1. Install Mininet, Ryu Controller, xterm, VLAN and Bridge contol as needed. Installing from packages is the easiest way.
  *  [Mininet](http://mininet.org/download/)
  * `pip install ryu` (  [Ryu Controller](https://ryu.readthedocs.io/en/latest/getting_started.html) )
  * `sudo apt-get install vlan`
  * `sudo apt-get install bridge-utils`
  * `sudo apt-get install xterm`
2. run ryu-controller and mininet
  * `sudo -E mn --topo single,16 --nat --mac --switch ovsk --controller remote -x`
  * `ryu-manager ./simple13_igmp_added.py ryu.app.ofctl_rest`
3. test igmp join and multicast messages

use [ryu controller source](../snippets/switch/snooping.py)

use [igmp code](../snippets/basic/igmp.py)
