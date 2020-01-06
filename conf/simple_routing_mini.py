from mininet.topo import Topo

class MyTopo (Topo):
    def __init__(self):
        Topo.__init__(self)

        ahost = self.addHost('h1')
        rhost = self.addHost('h2')
        bhost = self.addHost('h3')

        self.addLink(ahost, rhost)
        self.addLink(rhost, bhost)
topos = { 'mytopo' : (lambda: MyTopo() )}
