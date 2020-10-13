import csv
import os
import time

from TheProject.PcapConverter import *

PathHTTPS = "/home/nadeem/Documents/recorded_traffic_test/HTTPS"
PathDoH = "/home/nadeem/Documents/recorded_traffic_test/DoH"
# PathHTTPS = "/media/cyberlab/D/Desktop/Nour-FP/traffic records/splitted HTTPS_"
# PathDoH = "/media/cyberlab/D/Desktop/Nour-FP/traffic records/splitted DoH_"

def createcsv(name="DataSet"):
    filename = name + ".csv"
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Label', 'Duration', 'Average Time Delay', 'Min Time Delay',
                        'Max Time Delay', 'Percentage Incoming Packets', 'Percentage Outgoing Packets',
                         'Max Packet Size', 'Outgoing Packet Variance', 'Incoming Packet Variance',
                         'Average Outgoing Packets', 'Average Incoming packets', 'Ratio Bytes Size', 'Ration Of Packets'])
    return filename


def writeover(filename, type_pcap, duration, average_time_delay, min_time_delay, max_time_delay,
              percentage_incoming_packets, percentage_outgoing_packets, max_packet_size, outgoing_packet_variance,
              incoming_packet_variance, average_outgoing_packets, average_incoming_packets, ratio_bytes_size, ration_of_packets):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([type_pcap, duration, average_time_delay, min_time_delay, max_time_delay,
                         percentage_incoming_packets, percentage_outgoing_packets, max_packet_size,
                         outgoing_packet_variance, incoming_packet_variance, average_outgoing_packets,
                         average_incoming_packets, ratio_bytes_size, ration_of_packets])


def run(filename, type_pcap, path):
    filelist = os.listdir(path)
    random.shuffle(filelist)
    i = 0
    for pck in filelist:
        if i == 25000:
            break
        if (i % 100) == 0:
            print(i, '/25000')
        if pck.endswith(".pcap"):
            packets = rdpcap(path + "/" + pck)
            start = startin(path + "/" + pck)
            packet_list = pcaptolist(packets, start, 10)
            if len(packet_list) > 0:
                i += 1
                duration = durations(packet_list)
                src = packets[0].src
                time_packets = times(packet_list)
                num_packets = numpacket(packet_list, src)
                max_packet_size = maxpacket(packet_list)
                variance_size = variance(packets, src)
                average_size = average_way(packets, src)
                ratio_bytes_size = ratio_bytes(packets, src)
                ration_of_packets = ration_packets(packets, src)
                writeover(filename, type_pcap, duration, time_packets[0], time_packets[1], time_packets[2],
                          num_packets[0], num_packets[1], max_packet_size, variance_size[0], variance_size[1],
                          average_size[0], average_size[1], ratio_bytes_size, ration_of_packets)

x = createcsv()
run(x, 0, PathDoH)
run(x, 1, PathHTTPS)



# 24,381    Doh
# 761,542 HTTPS -> 25,000
