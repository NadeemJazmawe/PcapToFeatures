from scapy.all import *


# This function accept pcap file and it return number of packets in it
def numpcap(pck):
    return len(pck)


# this function accept pcap file , this function calculate the size of the file and return it
def sizepcap(pck):
    sum = 0;
    for packet in pck:
        sum += packet.__len__()
    return sum


# This function accept pcap file and calculate the average size of packets in it
def average(pck):
    return sizepcap(pck)/numpcap(pck)


# This function accept list of packets
# it return max packet size on this list
def maxpacket(pck):
    max = 0
    for packet in pck:
        if max < packet.__len__():
            max = packet.__len__()
    return max

# this function check where is first packet after the handshake
# and the key Exchange , and return the number of it
def startin(pck):
    return 15

def endin(pck):
    return pck.__len__()-3

# this function convert the pcap file to list
# every cell in this list will have one packet
# i have took only the first 30 packet after the key exchange(or less) to complete my research
def pcaptolist(pck):
    start = startin(pck)
    end = endin(pck)
    list = []
    i = 0
    for packet in pck:
        if (i == 30) or (i == end):
            break
        list.append(packet)
        i += 1
    return list


# this function accept list of packets
# it calculate the time between two packets , and return the average , min and max time
def times(pck):
    help = 0
    max = 0
    min = 99999999999
    average = 0
    for p in pck:
        if help == 0:
            help = p.time
        else:
            time = int((p.time - help) * 1000000)
            help = p.time
            if max < time:
                max = time
            elif min > time:
                min = time
            average += time

    average = int(average / 29)
    return [average, max, min]

def numpacket(pck, source):
    num = 0
    for packet in pck:
        if packet.src == source:
            num += 1
    num = num/len(pck)
    return [num, 1-num]




