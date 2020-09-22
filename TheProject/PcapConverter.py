from scapy.all import *


# first feature , is the num of packets in every pcap file
def numpcap(pck):
    return len(pck)


# second feature , size of the pcap file
def sizepcap(pck):
    sum = 0;
    for packet in pck:
        sum += packet.__len__()
    return sum


