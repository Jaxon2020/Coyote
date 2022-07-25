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










@click.group()
def cli():
    """Command Line tool to access group zero's API.
    
    Description and usage of commands:
    
    md5 -> Entering this command will send a get request to the /md5/ endpoint. This endpoint expects a input and will return the hashdata for that input.
    fibonacci -> Entering this command will send a get request to the /fibonacci/ endpoint. This endpoint expects a input and will return the fibonacci output for that input.
    factorial -> Entering this command will send a get request to the /factorial/ endpoint. This endpoint expects a input and will return the factorial output for that input.
    isprime -> Entering this command will send a get request to the /isprime/ endpoint. This endpoint expects a input and will see if the given input is prime or not.
    KEYVAL commands:
    keyvalsend -> Entering this commanding will send a post request to /keyval/ endpoint. This command will execute a function that will ask the user for two inputs: key and value. It will then also ask the user for a url.
    keyvalupdate -> Entering this commanding will send a put request to /keyval/ endpoint. This command will execute a function that will ask the user for two inputs: key and value. It will then also ask the user for a url.
    keyvalget -> Entering this commanding will send a get request to /keyval/ endpoint. This command will execute a function that will ask the user for one input as well as a url.
    keyvaldelete -> Entering this commanding will send a delete request to /keyval/ endpoint.  This command will execute a function that will ask the user for one input as well as a url.
    """
    pass

@cli.command()
def NMAP():
    print("Starting NMAP scan! This may take some time!")
    try: 
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
    except:
        print("Error!")



@cli.command()
def keyvaldelete():
    key = input('Key: ')
    url = input('Url: ')
   
    print(key, url)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////NMAP//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

