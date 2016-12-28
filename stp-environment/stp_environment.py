from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        Topo.__init__( self )
        switch_1 = self.addSwitch('s1')
        host_1_1 = self.addHost('h1_1')
        host_1_2 = self.addHost('h1_2')

        switch_2 = self.addSwitch('s2')
        host_2_1 = self.addHost('h2_1')

        switch_3 = self.addSwitch('s3')

        switch_4 = self.addSwitch('s4')
        host_4_1 = self.addHost('h4_1')

        switch_5 = self.addSwitch('s5')
        host_5_1 = self.addHost('h5_1')
        host_5_2 = self.addHost('h5_2')

        switch_6 = self.addSwitch('s6')
        host_6_1 = self.addHost('h6_1')

        switch_7 = self.addSwitch('s7')

        switch_8 = self.addSwitch('s8')
        host_8_1 = self.addHost('h8_1')

        switch_9 = self.addSwitch('s9')
        host_9_1 = self.addHost('h9_1')
        host_9_2 = self.addHost('h9_2')

        # Add links
        #1
        self.addLink( switch_1, host_1_1 )
        self.addLink( switch_1, host_1_2 )
        self.addLink( switch_1, switch_2 )
        self.addLink( switch_1, switch_4 )
        #2
        self.addLink( switch_2, host_2_1 )
        self.addLink( switch_2, switch_3 )
        self.addLink( switch_2, switch_5 )
        #3
        self.addLink( switch_3, switch_6 )
        #4
        self.addLink( switch_4, host_4_1 )
        self.addLink( switch_4, switch_5 )
        self.addLink( switch_4, switch_7 )
        #5
        self.addLink( switch_5, host_5_1 )
        self.addLink( switch_5, host_5_2 )
        self.addLink( switch_5, switch_6 )
        self.addLink( switch_5, switch_8 )
        #6
        self.addLink( switch_6, host_6_1 )
        self.addLink( switch_6, switch_9 )
        #7
        self.addLink( switch_7, switch_8 )
        #8
        self.addLink( switch_8, host_8_1 )
        self.addLink( switch_8, switch_9 )
        #9
        self.addLink( switch_9, host_9_1 )
        self.addLink( switch_9, host_9_2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
