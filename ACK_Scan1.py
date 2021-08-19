from scapy.all import * 
ip1 = IP(src="192.168.0.10", dst ="192.168.0.3" )
tcp1 = TCP(sport =1024, dport=137, flags="A", seq=12345)
packet = ip1/tcp1 
p =sr1(packet, inter=1) 
p.show()