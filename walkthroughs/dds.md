```
sudo -E mn --topo single,16 --nat --mac --switch ovsk --controller remote -x

source setenv.sh

$DDS_ROOT/bin/DCPSInfoRepo -ORBListenEndpoints iiop://10.0.0.16:12345

subscriber -DCPSConfigFile dds_sub_test.ini

publisher -DCPSConfigFile dds_pub_test.ini

======================dds_sub_test.ini==================

# This "common" section configures the data in Service_Participant. 
[common]

# Debug Level
DCPSDebugLevel=0

# IOR of DCPSInfoRepo process.
DCPSInfoRepo=corbaloc::10.0.0.16:12345/DCPSInfoRepo

# Sets the global transport configuration (used by default in the
# process to config1, defined below
DCPSGlobalTransportConfig=config1


# Transport configuration named config1, contains a single transport
# instance named tcp1 (defined below)
[config/config1]
transports=tcp1


# Transport instance named tcp1, of type "tcp".  Uses defaults for
# all configuration paramaters.
[transport/tcp1]
transport_type=tcp
local_address=10.0.0.15:


=======================rtps_sub.ini=================
[common]
#DPCSGlobalTransportConfig=$file
DCPSDefaultDiscovery=TheRTPSConfig
DCPSGlobalTransportConfig=myconfig

#[domain/4]
#DiscoveryConfig=uni_rtps

[rtps_discovery/TheRTPSConfig]
SedpMulticast=0
ResendPeriod=2
SedpLocalAddress=10.0.0.15:34567
SpdpSendAddrs=10.0.0.14:55555
SpdpLocalAddress=10.0.0.15

[config/myconfig]
transports=myrtpsudp

[transport/myrtpsudp]
transport_type=rtps_udp
use_multicast=0
local_address=10.0.0.15:34565
```
