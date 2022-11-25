#!/bin/bash

echo "give me a bottle of rum!"


echo "test run"


if [[ $# -eq 0 ]]
then
	echo -e "You need to specify the target domain.\n"
	echo -e "Usage:"
	echo -e "\t$0 <domain>"
	exit 1
else
    echo "Prepare for the enums!"

if [ $2 -eq S ]
then
    echo "INTIATING STEALTH SCAN, SNEAKY BOI"
    sudo nmap -sS -Pn --disable-arp-ping -vv -n $1
elif [ $2 -eq A ]
then
    echo "INTIATING AGGRESSIVE SCAN, LIVE FAST DIE HARD"
    sudo nmap -A -vv $1

elif [ $2 -eq SV ]
then
    echo "INTIATING STEALTH 'N VERSION SCAN, YE"
    sudo nmap -sS -sV -Pn --disable-arp-ping -vv -n $1 
else 
    echo "Ugh, no input? Or Error maybe"
fi

fi