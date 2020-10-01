from scapy.all import *

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


# To show num of packet in pcap file we use the method of __len__() , like the following line:
# print("the num of packets in pcap file is:", pck.__len__())
# To show the size of some packet in this pcap file
# print("size of the third packet", packets[1].__len__())
# To show info of any packet
print(pck.show())
# we can also show only one info of the packet like this
print(pck.src)
print(pck.time)
