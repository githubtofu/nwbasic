## unicast switching ##

Run ryu controller : `ryu-manager --verbose ./simple_switch_13.py`

Run mininet with 10 hosts: `sudo mn --topo single,10 --mac --controller remote --switch ovsk -x`

Run wireshark on host 1 and 2 and 3 and 4

On mininet terminal, check flows : `dpctl dump-flows`

Note input conditions and output ports.

Ping from host 1 to host 2

On mininet terminal, check flows and note changes in number of packets and bytes on corresponding flows.

On mininet terminal, delete all flows : `dpctl del-flows`

Ping from host 1 to host 2 and check corresponding packets on wireshark

On mininet terminal, add a flow for broadcast: `dpctl add-flow dl_dst=ff:ff:ff:ff:ff:ff,action=FLOOD`

Ping from host 1 to host 2 and check corresponding packets on wireshark

On mininet terminal, add a flow to host 1: `dpctl add-flow dl_dst=<<MAC address of host 1>>,action=1`

Ping from host 1 to host 2 and check corresponding packets on wireshark

On mininet terminal, add a flow to host 2: `dpctl add-flow dl_dst=<<MAC address of host 2>>,action=2`

Ping from host 1 to host 2 and check corresponding packets on wireshark

## multicast switching ##

Add default gateway 


