Run ryu controller : `ryu-manager --verbose ./simple_switch_13.py`

Run mininet with 10 hosts: `sudo mn --topo single,10 --mac --controller remote --switch ovsk -x`

Run wireshark on host 1 and 2 and 3

On mininet terminal, check flows : `dpctl dump-flows`
