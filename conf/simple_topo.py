from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple two if example."

    def __init__(self):
        
        Topo.__init__( self )

        chost = self.addHost( 'h1' )
        lhost = self.addHost( 'h2' )
        rhost = self.addHost( 'h3' )
        lswitch = self.addSwitch( 's3' )
        rswitch = self.addSwitch( 's4' )

        self.addLink( lhost, lswitch )
        self.addLink( chost, lswitch )
        self.addLink( chost, rswitch )
        self.addLink( rhost, rswitch )

topos = { 'mytopo' : ( lambda: MyTopo() ) }
