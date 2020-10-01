import csv
import os

from TheProject.PcapConverter import *

PathHTTPS = "/home/nadeem/Documents/recorded_traffic_test/HTTPS"
PathDoH = "/home/nadeem/Documents/recorded_traffic_test/DoH"


def createcsv(name="DataSet"):
    filename = name + ".csv"
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['type Pcap', 'client packets', 'dist packets', 'average time to packet', 'max packet time',
                        'min packet time', 'average'])
    return filename


def writeover(filename, col1, col2, col3, col4, col5, col6, col7):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([col1, col2, col3, col4, col5, col6, col7])


def run(filename, type_pcap, path):
    filelist = os.listdir(path)
    for pck in filelist:
        if pck.endswith(".pcap"):
            packets = rdpcap(path + "/" + pck)
            if (packets.__len__() > 50):
                packet_list = pcaptolist(packets)
                time_packets = times(packet_list)
                num_packets = numpacket(packet_list, packets[0].src)
                max_packet_size = maxpacket(packet_list)
                writeover(filename, type_pcap, num_packets[0], num_packets[1], time_packets[0], time_packets[1],
                          time_packets[2], max_packet_size)


x = createcsv()
run(x, 0, PathDoH)
run(x, 1, PathHTTPS)
