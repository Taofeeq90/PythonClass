from scapy.all import * 
ip1 = IP(src="192.168.0.99", dst ="127.0.0.1") 
packet = ip1/ICMP()/("m"*60000) 
send(packet) 