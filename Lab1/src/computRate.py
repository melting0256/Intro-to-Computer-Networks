
from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys
import time

# get path of pcap file
INPUTPATH_TCP1 = sys.argv[1]
INPUTPATH_TCP2 = sys.argv[2]
INPUTPATH_UDP1 = sys.argv[3]
INPUTPATH_UDP2 = sys.argv[4] 

# read pcap
packets_TCP1 = rdpcap(INPUTPATH_TCP1)
packets_TCP2 = rdpcap(INPUTPATH_TCP2)
packets_UDP1 = rdpcap(INPUTPATH_UDP1)
packets_UDP2 = rdpcap(INPUTPATH_UDP2) 


# print ("***Print all packets in this pcap file***")
# print (packets.show())
# print ("***Print all TCP packets in this pcap file***")
# print (packets[TCP].show())
# print ("***Print the first TCP packet content***")
# print (packets[TCP][0].show())
# print ("***Get data of this packet***")
# print ("src IP: ", packets[TCP][0][1].src) # in IP layer
# print ("dst IP: ", packets[TCP][0][1].dst) # in IP layer
# print ("src port: ", packets[TCP][0][2].sport) # in TCP layer
# print ("dst port: ", packets[TCP][0][2].dport) # in TCP layer
# print ("packet size: ", len(packets[TCP][0]), " bytes")
# print ("***Count number of TCP packets***")
# count = 0
# for packet in packets[TCP]:
#     count += 1
# print ("number of TCP packets: ", count)

# firstTime_TCP1 = time.time()
t = 0
length_TCP1 = 0

for packet in packets_TCP1[TCP]:
    # if (packets_TCP1[TCP][t][2].dport==7777) :
    length_TCP1 += len(packets_TCP1[TCP][t])
    t += 1
# endTime_TCP1 = time.time()
# totalTime_TCP1 = endTime_TCP1 - firstTime_TCP1
totallength_TCP1 = length_TCP1 * 8
# flow_TCP1 = (totallength_TCP1 / totalTime_TCP1) / 5000000
flow_TCP1 = totallength_TCP1 / 5000000

# firstTime_TCP2 = time.time()
t = 0
length_TCP2 = 0
for packet in packets_TCP2[TCP]:
#   if (packets_TCP2[TCP][t][2].dport==7777) :
    length_TCP2 += len(packets_TCP2[TCP][t])
    t += 1
# endTime_TCP2 = time.time()
# totalTime_TCP2 = endTime_TCP2 - firstTime_TCP2
totallength_TCP2 = length_TCP2 * 8
# flow_TCP2 = (totallength_TCP2 / totalTime_TCP2)/1000000
flow_TCP2 = totallength_TCP2 / 5000000


print (" --- TCP --- ")
print ("Flow1(h1->h4):  ", flow_TCP2 , "Mbps")
print ("Flow3(h2->h3):  ", flow_TCP1 , "Mbps")


# firstTime_UDP1 = time.time()
t = 0
length_UDP1 = 0
for packet in packets_UDP1[UDP]:
    # if (packets_UDP1[UDP][t][2].dport==7777) :
    length_UDP1 += len(packets_UDP1[UDP][t])
    t += 1
# endTime_UDP1 = time.time()
# totalTime_UDP1 = endTime_UDP1 - firstTime_UDP1
totallength_UDP1 = length_UDP1 * 8
# flow_UDP1 = (totallength_UDP1 / totalTime_UDP1) / 1000000
flow_UDP1 = totallength_UDP1 / 5000000

# firstTime_UDP2 = time.time()
t = 0
length_UDP2 = 0
for packet in packets_UDP2[UDP]:
    # if (packets_UDP2[UDP][t][2].dport==7777) :
    length_UDP2 += len(packets_UDP2[UDP][t])
    t += 1
# endTime_UDP2 = time.time()
# totalTime_UDP2 = endTime_UDP2 - firstTime_UDP2
totallength_UDP2 = length_UDP2 * 8
# flow_UDP2 = (totallength_UDP2 / totalTime_UDP2) / 1000000
flow_UDP2 = totallength_UDP2 / 5000000

print (" --- UDP --- ")
print ("Flow1(h1->h4):  ", flow_UDP2 , "Mbps")
print ("Flow3(h2->h3):  ", flow_UDP1 , "Mbps")