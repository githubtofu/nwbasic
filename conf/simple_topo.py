from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple two if example."

    def __init__(self):
        
        Topo.__init__( self )

        lhost = self.addHost( 'h1' )
        rhost = self.addHost( 'h2' )
        ahost = self.addHost( 'h3' )
        lswitch = self.addSwitch( 's3' )
        rswitch = self.addSwitch( 's4' )

        self.addLink( lhost, lswitch )
        self.addLink( lhost, rswitch )
        self.addLink( rhost, rswitch )
        self.addLink( ahost, lswitch )

topos = { 'mytopo' : ( lambda: MyTopo() ) }
