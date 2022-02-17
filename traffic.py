import scapy.all as scapy
from scapy.all import IP
import os
import sys
import subprocess


if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()






IPlist = []
IPset = {}

def IPstore(pkt):
    for i in range(len(pkt)):
        try:
            IPlist.append(pkt[i][1].src)
            IPlist.append(pkt[i][1].dst)
            print("Sender: ", pkt[i][1].src, "Receiver: ", pkt[i][1].dst, "Protocol", pkt[i][1].proto)

        except: 
            continue
            
pkt = scapy.sniff(count=10, iface='wlp5s0', prn=IPstore)

IPset = set(IPlist)

print(IPlist)
print(IPset)

