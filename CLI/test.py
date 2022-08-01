from telnetlib import IP
from scapy.all import *
import time


def listen_dhcp():
    # Make sure it is DHCP with the filter options
    pkt = sniff(prn=print_packet, filter='udp and (port 67 or port 68)')
    pkt.summary()


def print_packet(packet):
    # initialize these variables to None at first
    pkt = packet

    target_mac, requested_ip, hostname, vendor_id = [None] * 4
    # get the MAC address of the requester
    if pkt.haslayer(IP):
        target_mac = pkt.getlayer(IP).src
    # get the DHCP options
    dhcp_options = pkt[IP]
    for item in dhcp_options:
        try:
            label, value = item
        except ValueError:
            continue
        if label == 'requested_addr':
            # get the requested IP
            requested_ip = value
        elif label == 'hostname':
            # get the hostname of the device
            hostname = value.decode()
        elif label == 'vendor_class_id':
            # get the vendor ID
            vendor_id = value.decode()
    if target_mac and vendor_id and hostname and requested_ip:
        # if all variables are not None, print the device details
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")


if __name__ == "__main__":
    listen_dhcp()