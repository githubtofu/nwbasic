# Setting
* download package and install

download and install
* ping test

ping test

# Host Configuration

```
h1 ifconfig h1-eth0 10.0.2.0 netmask 255.0.0.0
h1 sudo macchanger -m 02:00:00:00:02:00 h1-eth0
h1 route add default gw 10.0.0.17 h1-eth0
h1 echo 2 > /proc/sys/net/ipv4/conf/h1-eth0/force_igmp_version
h1 ECUEm.x86_64 --ecu=ICU
h2 ifconfig h2-eth0 10.0.1.0 netmask 255.0.0.0
h2 sudo macchanger -m 02:00:00:00:01:00 h2-eth0
h2 route add default gw 10.0.0.17 h2-eth0
h2 echo 2 > /proc/sys/net/ipv4/conf/h2-eth0/force_igmp_version
h2 ECUEm.x86_64 --ecu=H_U
h3 ifconfig h3-eth0 10.0.0.128 netmask 255.0.0.0
h3 sudo macchanger -m 02:00:00:00:00:80 h3-eth0
h3 route add default gw 10.0.0.17 h3-eth0
h3 echo 2 > /proc/sys/net/ipv4/conf/h3-eth0/force_igmp_version
h3 ECUEm.x86_64 --ecu=CLU
h4 ifconfig h4-eth0 10.0.0.64 netmask 255.0.0.0
h4 sudo macchanger -m 02:00:00:00:00:40 h4-eth0
h4 route add default gw 10.0.0.17 h4-eth0
h4 echo 2 > /proc/sys/net/ipv4/conf/h4-eth0/force_igmp_version
h4 ECUEm.x86_64 --ecu=HUD
h5 ifconfig h5-eth0 10.0.0.32 netmask 255.0.0.0
h5 sudo macchanger -m 02:00:00:00:00:20 h5-eth0
h5 route add default gw 10.0.0.17 h5-eth0
h5 echo 2 > /proc/sys/net/ipv4/conf/h5-eth0/force_igmp_version
h5 ECUEm.x86_64 --ecu=DVRS
h6 ifconfig h6-eth0 10.0.0.16 netmask 255.0.0.0
h6 sudo macchanger -m 02:00:00:00:00:10 h6-eth0
h6 route add default gw 10.0.0.17 h6-eth0
h6 echo 2 > /proc/sys/net/ipv4/conf/h6-eth0/force_igmp_version
h6 ECUEm.x86_64 --ecu=ADAS_PRK
h7 ifconfig h7-eth0 10.0.0.8 netmask 255.0.0.0
h7 route add default gw 10.0.0.17 h7-eth0
h7 echo 2 > /proc/sys/net/ipv4/conf/h7-eth0/force_igmp_version
h7 ECUEm.x86_64 --ecu=RR_CMR
h8 ifconfig h8-eth0 10.0.0.4 netmask 255.0.0.0
h8 sudo macchanger -m 02:00:00:00:00:04 h8-eth0
h8 route add default gw 10.0.0.17 h8-eth0
h8 echo 2 > /proc/sys/net/ipv4/conf/h8-eth0/force_igmp_version
h8 ECUEm.x86_64 --ecu=SR_FR_CMR
h9 ifconfig h9-eth0 10.0.0.2 netmask 255.0.0.0
h9 sudo macchanger -m 02:00:00:00:00:02 h9-eth0
h9 route add default gw 10.0.0.17 h9-eth0
h9 echo 2 > /proc/sys/net/ipv4/conf/h9-eth0/force_igmp_version
h9 ECUEm.x86_64 --ecu=SR_SD_CMR_LH
h10 ifconfig h10-eth0 10.0.0.1 netmask 255.0.0.0
h10 sudo macchanger -m 02:00:00:00:00:01 h10-eth0
h10 route add default gw 10.0.0.17 h10-eth0
h10 echo 2 > /proc/sys/net/ipv4/conf/h10-eth0/force_igmp_version
h10 ECUEm.x86_64 --ecu=SR_SD_CMR_RH
h11 ifconfig h11-eth0 10.0.4.0 netmask 255.0.0.0
h11 sudo macchanger -m 02:00:00:00:04:00 h11-eth0
h11 route add default gw 10.0.0.17 h11-eth0
h11 echo 2 > /proc/sys/net/ipv4/conf/h11-eth0/force_igmp_version
h11 ECUEm.x86_64 --ecu=ESU
h16 ifconfig h16-eth0 10.1.1.1
h16 sudo macchanger -m 00:00:00:01:01:01 h16-eth0
h16 route add default gw 10.0.0.17 h16-eth0
h16 echo 2 > /proc/sys/net/ipv4/conf/h16-eth0/force_igmp_version
h16 ECUEm.x86_64 --ecu=ERT
```
