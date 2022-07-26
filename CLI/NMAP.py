#!/usr/bin/env python3

import subprocess
import nmap
from numpy import empty
import pandas as ps
import os
from shlex import *
import sqlite3 as sql
import parsedata
import click










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
