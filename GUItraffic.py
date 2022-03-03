import PySimpleGUI as sg
import scapy.all as scapy
import os, subprocess, sys
from subprocess import run





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

def IPtracker(count):
    
    #if os.geteuid() == 0:
    #  print("We're root!")
    #else:
    #  print("We're not root.")
    # text = sg.popup_get_text('SUDO', 'Please enter sudo password')
    #  print(text)
    #  data = bytes(text, 'utf-8')
    #  run(['echo', data, '|','sudo', '-S' ,'python3', *sys.argv], input=data)
    #  sys.exit()

    
    pkt =  scapy.sniff(count=count, prn=IPstore)
    IPset = set(IPlist)

    print(IPlist)
    print(IPset)

def main():
    sg.theme('DarkAmber')
    layout = [[sg.Text('IP Tracker', font='Default 18')],
              [sg.T('Count Amount', size=(8,1)), sg.Input(key='-Count-', size=(35,1))],
              [sg.Button('Send'), sg.Button('Exit')]]

    window = sg.Window('IP Tracker', layout, icon=icon, no_titlebar=False)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Send':
            if sg.__name__ != 'PySimpleGUIWeb':     # auto close popups not yet supported in PySimpleGUIWeb
                sg.popup_quick_message('Running IPtracker... this will take a moment...', background_color='red')
            
            IPtracker(count=int(values['-Count-']))
                          

    window.close()

if __name__ == '__main__':

    icon = 'images/IMG-0886.PNG'
    main()
