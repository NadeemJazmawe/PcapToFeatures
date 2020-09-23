import csv
import os

from TheProject.PcapConverter import *

PathHTTPS = "/home/nadeem/Documents/recorded_traffic_test/HTTPS"
PathDoH = "/home/nadeem/Documents/recorded_traffic_test/DoH"


def createcsv(name="DataSet"):
    filename = name + ".csv"
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['type Pcap', 'num of packets', 'size of packets', 'average'])
    return filename


def writeover(filename, col1, col2, col3, col4):
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([col1, col2, col3, col4])


def run(filename, pathdoh, pathttps):
    filelist = os.listdir(pathdoh)
    for pck in filelist:
        if pck.endswith(".pcap"):
            packets = rdpcap(pathdoh + "/" +pck)
            n = numpcap(packets)
            s = sizepcap(packets)
            writeover(filename, 0, n, s, s/n)

    filelist = os.listdir(pathttps)
    for pck in filelist:
        if pck.endswith(".pcap"):
            packets = rdpcap(pathttps + "/" + pck)
            n = numpcap(packets)
            s = sizepcap(packets)
            writeover(filename, 1, n, s, s/n)


x = createcsv()
run(x, PathDoH, PathHTTPS)
