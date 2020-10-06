from scapy.all import *
import numpy as np
import pyshark

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
    return sizepcap(pck) / numpcap(pck)


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
def startin(path_doh_session):
    pcap_file = pyshark.FileCapture(path_doh_session)
    server_ip_src = str(pcap_file[0].ip.dst)
    index = 0
    for packet in pcap_file:
        index += 1
        for layer in packet.layers:
            if layer._field_prefix == 'tls.':
                st = str(layer)
                if (("TLSv1.3 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec" in st)
                        or ("TLSv1.2 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec" in st)
                        and (str(
                            packet.ip.src) == server_ip_src)):  # for the correct Encripted Handshake Message from the server.
                    pcap_file.close()
                    return index + 1
    return -1


def endin(pck):
    return pck.__len__() - 4


# this function convert the pcap file to list
# every cell in this list will have one packet
# i have took only the first 30 packet after the key exchange(or less) to complete my research
def pcaptolist(pck, start, length=30):
    end = min(endin(pck), start+length)
    list = []
    if start == -1:
        return list
    for i in range(start, end):
        if i == end:
            break
        list.append(pck[i])
    print(len(list))
    return list


# This function accept pcap file
# it calculate and return the time that this pcap file took
def durations(pck):
    start = pck[0].time
    end = pck[-1].time
    return end - start


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
            if min > time:
                min = time
            average += time

    average = int(average / (len(pck)))
    return [average, min, max]


# This function accept list of packets and ip of the source
# it calculate the percentage of incoming and outgoing packets
# it return it in a list
def numpacket(pck, source):
    num = 0
    for packet in pck:
        if packet.src == source:
            num += 1
    if pck.__len__() == 0:
        num = 0
    else:
        num = num / pck.__len__()
    return [num, 1 - num]


# This function accept list of packets and the source ip
# and it calculate the variance of the incoming/outgoing packets
def variance(pck, src):
    list_incoming = []
    list_outgoing = []
    for packet in pck:
        if packet.src == src:
            list_outgoing.append(packet.__len__())
        else:
            list_incoming.append(packet.__len__())

    outgoing_variance = np.var(list_outgoing)
    incoming_variance = np.var(list_incoming)
    return [outgoing_variance, incoming_variance]


# This function accept pcap file and the source ip
# it calculate the average of incoming/outgoing packets
def average_way(pck, src):
    list_incoming = []
    list_outgoing = []
    for packet in pck:
        if packet.src == src:
            list_outgoing.append(packet.__len__())
        else:
            list_incoming.append(packet.__len__())

    outgoing_av_size = np.average(list_outgoing)
    incoming_av_size = np.average(list_incoming)
    return [outgoing_av_size, incoming_av_size]


# This function accept pcap file and the source ip
# it calculate the ratio bytes between the incoming and outgoing packets
def ratio_bytes(pck, src):
    list_incoming = []
    list_outgoing = []
    for packet in pck:
        if packet.src == src:
            list_outgoing.append(packet.__len__())
        else:
            list_incoming.append(packet.__len__())

    outgoing_size = np.sum(list_outgoing)
    incoming_size = np.sum(list_incoming)
    if incoming_size == 0:
        return 1
    return outgoing_size/incoming_size


# This function accept pcap file and the source ip
# it calculate the ration number of the incoming and outgoing packets
def ration_packets(pck, src):
    list_incoming = []
    list_outgoing = []
    for packet in pck:
        if packet.src == src:
            list_outgoing.append(packet.__len__())
        else:
            list_incoming.append(packet.__len__())

    if len(list_incoming) == 0:
        return 1
    return len(list_outgoing)/len(list_incoming)
