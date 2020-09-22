from TheProject.PcapConverter import *

print("over Https:")
pc1 = rdpcap("HTTPS-0002.pcap")
x1 = numpcap(pc1)
y1 = sizepcap(pc1)
s1 = y1/x1
print("number of packets in pcap file is ", x1)
print("the size of our pcap file is", y1)
print("average size of packets", s1)

print("over DoH:")
pc2 = rdpcap("DoH-0016.pcap")
x2 = numpcap(pc2)
y2 = sizepcap(pc2)
s2 = y2/x2
print("number of packets in pcap file is ", x2)
print("the size of our pcap file is", y2)
print("average size of packets", s2)



