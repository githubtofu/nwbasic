from mininet.topo import Topo

class MyTopo (Topo):
    def __init__(self):
        Topo.__init__(self)

        ahost = self.addHost('h1')
        rhosta = self.addHost('h2')
        rhostb = self.addHost('h3')
        bhost = self.addHost('h4')

        self.addLink(ahost, rhosta)
        self.addLink(rhosta, rhostb)
        self.addLink(rhostb, bhost)
        
topos = { 'mytopo' : (lambda: MyTopo() )}
