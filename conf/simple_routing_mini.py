from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from subprocess import call
import time, os

net = Mininet(controller=None, link=TCLink, autoSetMacs=True)
print "***Creating nodes..."
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
print "***Creating links..."
net.addLink(h1, h2)
net.addLink(h2, h3)
net.start()
CLI(net)
net.stop()
