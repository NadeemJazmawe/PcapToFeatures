# PcapToFeatures

This code for extracts features for pcap files.

it has writed with <b>Pythom</b>.

it run automatically and save the features in <b>csv</b> format.

# Features you can get with:
* Duration: Time frame during the session.
* Average time delay: Average delay time for each packet in the session.
* Max time delay: Maximum delay time for a single packet in the session.
* Min time delay: Minimum delay time for a single packet in the session.
* Percentage incoming packets: Percent of packets received in the session.
* Percentage outgoing packets: Percent of packets sent in the session.
* Max packet size: Maximum size of a single packet in the session.
* Outgoing packet variance: Variance of packets size received in the session.
* Incoming packet variance: Variance of packets size sent in the session.
* Average outgoing packets: Average size of packets sent in the session.
* Average incoming packets: Average size of packets received in the session.
* Ratio Bytes Size: Ratio between sending and receiving bytes.
* Ration Of Packets: Ratio between number of packets sent and number of packets received.

# Installation
you should install the code (the mean code can be found in <b>TheProject</b> folder), importing wrapper.py

```
import wrapper
```

creating <b>CSV file</b> using <b>createcsv</b> function with name of the file(or it will give automatically name to this file - DataSet).
```
  createcsv("file name")
```

also you can use any <b>CSV</b> file to write over
after that running the <b>run</b> function , you need to give it name of the CSV file you want to use and label number and path for the folder that have the PCAP files.
```
  run("file name", "label number", "path to folder")
```
 
* Example:
```
  x = createcsv()
  run(x, 0, PathDoH)
  run(x, 1, PathHTTPS)
```
 






* you can find exampels for PCAP files and the CSV file that will reseve in Example Folder.

It has been writed to comblete my research, you can use it for anything else..

Enjoy :P
