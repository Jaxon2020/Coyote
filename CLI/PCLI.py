#!/usr/bin/env python3
import argparse
import nmap
import os
import pandas as ps
from scapy.all import ARP, Ether, srp
import subprocess
import parsedata
import hashlib
import test






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
            print("The following are results that were found in the local nmap result file. Would you like to search for these, if not you must input your own args to pass to searchsploit!")
            oneorzero = input("Enter 1 for results and 0 for entering your own!: ")

            if oneorzero == 1:

                print(nmr['product'][0] + " " + nmr['version'][0])

                args1 = nmr['product'][0]

                args2 = nmr['version'][0]

                print(argsploit, args1, args2)
                output = subprocess.Popen([argsploit, str(args1), str(args2)], stdout=subprocess.PIPE).communicate()[0] 
                convertout = output.decode('utf-8')
            
                filetest = open('exploitdata.txt', 'w')
                filetest.write(str(convertout))
                filetest.close()

                print(parsedata.parsexdata())
            else:

                args1 = input("Enter Args1: ")

                args2 = input("Enter Args2: ")

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



def PPasswordCracker():

    print("**************PASSWORD CRACKER ******************")
            
    # To check if the password
    # found or not.
    pass_found = 0                                     
    
    input_hash = input("Enter the hashed password:")
    
    pass_doc = input("\nEnter passwords filename including path(root / home/):")
    
    try:
        # trying to open the password file.
        pass_file = open(pass_doc, 'r')             
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.")
        quit()
    
    
    # comparing the input_hash with the hashes
    # of the words in password file,
    # and finding password.
    
    for word in pass_file:
        # encoding the word into utf-8 format
        enc_word = word.encode('utf-8') 
                
        # Hashing a word into md5 hash
        hash_word = hashlib.md5(enc_word.strip())  
    
        # digesting that hash into a hexa decimal value    
        digest = hash_word.hexdigest()        
        
        if digest == input_hash:
            # comparing hashes
            print("Password found.\nThe password is:", word)  
            pass_found = 1
            break
    
    # if password is not found.
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")  
        print('\n')
    print("*****************  Thank you  **********************")

def DHCPEAR():
    test.listen_dhcp()



parser = argparse.ArgumentParser(description="A Cyber security tool that is aimed at being a general purpose tool.")
parser.add_argument('-nm',action='store_true', help='Network Mapper: NMAP - Used for scanning networks and computers. Can scan for hosts on a network and scan for open computer ports.');
parser.add_argument('-ns',action='store_true', help='A network scanner that uses ARP to scan the entire network of all devices and returns their IP and MAC address.');
parser.add_argument('-se',action='store_true', help='Searchsploit is a tool that will search up possible exploits on vulnerabilities based on the arguments you give.');
parser.add_argument('-pc',action='store_true', help='A simple password cracker that currently can only break MD5 hashes.');
parser.add_argument('-dear',action='store_true', help='A DHCP listner to monitor when new devices join the network. As well as collect valuable information on the hosts. ');
args = parser.parse_args()

if args.nm:
    NMAP()
if args.ns:
    NetworkScanner()
if args.se:
    SearchSploit()
if args.pc:
    PPasswordCracker()
if args.dear:
    DHCPEAR()
else:
    print("what")
    