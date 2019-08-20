1. Install [Mininet](http://mininet.org/download/) and [Ryu Controller](https://ryu.readthedocs.io/en/latest/getting_started.html)
2. Define Topology
  * see an example at conf directory : [Simple Topology](https://github.com/githubtofu/nwbasic/blob/master/conf/simple_topo.py)
  * save the topology python file as (for example) 'simple.py'
3. Define Switch Operation
  * save the switch code as (for example) 'switch.py'. The code is in the conf directory : [Code]()
4. Run Ryu Controller
  * `ryu-manager ./switch.py ryu.app.ofctl_rest`
5. Run Mininet on a separate terminal
  * `sudo mn --custom ./simple.py --topo mytopo --mac --switch ovsk --controller remote -x`
5. 
