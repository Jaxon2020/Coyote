#!/usr/bin/env python3
import argparse
import nmap
import os
import pandas as ps
from scapy.all import ARP, Ether, srp
import subprocess
import parsedata








def NMAP():
    print("Starting NMAP scan! This may take some time!")
     
    whatIP = input("Enter IP: ")
    INargs = input("Enter Args: ")
    nm = nmap.PortScanner()
    nm.scan(hosts=whatIP, arguments=INargs)
    
    if os.path.exists("nmapdump.csv"):
        os.remove("nmapdump.csv")
    else:
        print("The file does not exist")

    file = open('nmapdump.csv', 'a')
    file.write(nm.csv())
    file.close()
    test_data = ps.read_csv('nmapdump.csv', sep = ';', header = 0)

    print("\n"'Host: %s(%s)' % (whatIP, nm[whatIP].hostname()))
    print("\n"'State : %s' % nm[whatIP].state())


    print( "\n", test_data[['protocol', 'port', 'name', 'product', 'version', 'state', 'reason' ]])

    print("Error!")




def NetworkScanner():
    target_ip = input("Enter target IP: ")
    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    # print clients
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))






def SearchSploit():
        
    nmr = ps.read_csv('nmapdump.csv', sep = ';', header = 0)

    adinforesults = 0
                
    if adinforesults == 0:
        print("Checking for exploits based on nmap results.")
        try: 
            
            argsploit = "searchsploit"

            args1 = nmr['product'][0]

            args2 = nmr['version'][0]

            print(argsploit, args1, args2)
            output = subprocess.Popen([argsploit, str(args1), str(args2)], stdout=subprocess.PIPE).communicate()[0] 
            convertout = output.decode('utf-8')
        
            filetest = open('exploitdata.txt', 'w')
            filetest.write(str(convertout))
            filetest.close()

            print(parsedata.parsexdata())
        except:
            print("Error!")

    elif adinforesults == 1:
        print("Checking for exploits based upon nmap results and additional submitted info.")
    else:
        print("Checking for exploits based upon nmap results, web enumeration results, and additional submitted info.")







parser = argparse.ArgumentParser(description="Network Things.")
parser.add_argument('-nm',action='store_true');
parser.add_argument('-ns',action='store_true');
parser.add_argument('-se',action='store_true');
args = parser.parse_args()

if args.nm:
    NMAP()
if args.ns:
    NetworkScanner()
if args.se:
    SearchSploit()
else:
    print("what")
    