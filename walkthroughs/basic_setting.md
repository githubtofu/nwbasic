1. Install Mininet, Ryu Controller, xterm, VLAN and Bridge contol as needed. Installing from packages is the easiest way.
  * `sudo apt-get install mininet` [Mininet](http://mininet.org/download/)
  * `pip install ryu` and `sudo apt install python3-ryu` (  [Ryu Controller](https://ryu.readthedocs.io/en/latest/getting_started.html) )
  * `sudo apt-get install xterm`
 
2. Run ryu controller : `ryu-manager --verbose ./simple_switch_13.py` (conf file is on conf directory)

3. Run mininet with 3 hosts: `sudo mn --topo single,3 --mac --controller remote --switch ovsk -x`

4. Run wireshark on all hosts using main interfaces (for example, eth0 or h1-eth0)
