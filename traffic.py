import scapy.all as scapy
import os
import sys
import subprocess

if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()



pkt = scapy.sniff(count=1)





print(pkt.summary())
