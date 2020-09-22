from scapy.all import *

# # rdpcap comes from scapy and loads in our pcap file
# from scapy.layers.dns import DNSRR
#
# packets = rdpcap('HTTPS-0002.pcap')
# # str(packet)
#
# # Let's iterate through every packet
# for packet in packets:
#     print(packet)
#     # We're only interested packets with a DNS Round Robin layer
#     if packet.haslayer(DNSRR):
#         # If the an(swer) is a DNSRR, print the name it replied with.
#         if isinstance(packet.an, DNSRR):
#             print(packet.an.rrname)

# First we need to read the pcap file
# to read pcap file use rdpcap() function
packets = rdpcap("../TheProject/DoH-0016.pcap")
# packets is the name of our pcap file.


# To know how many packets we have in our pcap file , you can use len() function
print(len(packets))


# To analyze pcap file
# need to analyze single packet every time:
pck = packets[1]
# pck will be one packet of the packets in pcap file

# type() method returns a each packet as an object
# In below example it is returning object of type Ether
# print(type(pck))


# if you want to know which functions you can use on this packet
# use the dir() function
print(dir(pck))
# print(sizeof(pck))

# to print the packet you can use str() function
# print(str(pck))
# it have no sense...

# for will printing:
# hexdump() method can also be use for printing packets. it prints the information about source ,
# destination , timestamp , channel etc.
# hexdump(pck)


# To print full/complete information of each packet
# use show() function
# pck.show2()


# To show the length of the packet we use the method of __len__() , like the following line:
print("the size of the packet is:", pck.__len__())
