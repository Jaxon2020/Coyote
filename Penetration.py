from operator import index
import subprocess
from tkinter.tix import COLUMN
import PySimpleGUI as sg
import nmap
import pandas as ps
import os
import GUItraffic as Packets
import shlex

ninfo = open('nmapinfo.txt', 'r')
contents = ninfo.read()
ninfo.close()


def NMAP():

    sg.theme('DarkPurple6')

    layout = [
                [sg.Button("Exit", button_color=('white', 'firebrick3'))],
                [sg.Text('NMAP: Network Mapper'), sg.Button("Open Cheat Sheet", key="open")],
                [sg.Text('IP:'), sg.Input(key='-IP-',size=(20,1)), sg.Text('Options'), sg.Input(key='-ARGS-', size=(20,1))],
                [sg.Output(size=(100,30), key='-OUTPUT-')],
                [sg.Button("Send", key="-SEND-")],

            
                ]
    window = sg.Window("Main Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            if sg.Window("Other Window", [[sg.Text("Cheat Sheet")], 
                                          [sg.Text("Commonly used NMAP Options: ")], 
                                          [sg.Text(contents)],
                                          [sg.Yes(), sg.No()]]).read(close=True)[0] == "Yes":
                print("User chose yes!")
            else:
                print("User chose no!")
        if event == "-SEND-":

            try:
                print("Starting NMAP scan! This may take some time!")

                nm = nmap.PortScanner()
                nm.scan(hosts=values['-IP-'], arguments=values['-ARGS-'])
                list = nm.csv()


                if os.path.exists("nmapdump.csv"):
                    os.remove("nmapdump.csv")
                else:
                    print("The file does not exist")
                file = open('nmapdump.csv', 'a')
                file.write(nm.csv())
                file.close()
                test_data = ps.read_csv('nmapdump.csv', sep = ';', header = 0)

                print("\n"'Host: %s(%s)' % (values['-IP-'], nm[values['-IP-']].hostname()))
                print("\n"'State : %s' % nm[values['-IP-']].state())
                
                
                print( "\n", test_data[['protocol', 'port', 'name', 'state', 'reason']])
            except:
                print("Error!")
            

    window.close()


def EnumResults():

    sg.theme('DarkPurple6')

    ART = """
    
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,@@@@,,,,,,,,,@@@@,,,,,,,,,,,,
        ,,,,,,,,,,,@@@@@@@@@@@@@@@@@@,,,,,,,,,,,
        ,,,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,@,,,,@@@@@@@@,,,,,,,,,,
        ,,,,,,,,,,,,,,,,@@,,,,,,@@@@@@,,,,,,,,,,
        ,,,,,,,,,,,,,@@@@@@@@,,@@@@@@,,,,,,,,,,,
        ,,,,,,,,,,,,@@@@@@@@@@@@@,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,@@@@@@@,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    
    
        """

    layout = [
        
            
            


            [sg.Text("Coyote", size=(40, 1))],
            [sg.Text(ART)],
            [sg.Text("Results from enumeration")],
            [sg.Text("Waiting for Data", key='-P&S-')],
            [sg.Output(size=(30,10), key='-1OUT-')],
            [sg.Button("Display", key="-ESEND-", bind_return_key=True)],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='Exit') ]
            
            
            ]
    window = sg.Window("Results Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9, font=('Courier 15'))
    choice = None
    while True:
        event, values = window.read()
        if event == "-ESEND-":
            
            
            nmr = ps.read_csv('nmapdump.csv', sep = ';', header = 0)
            
            window['-P&S-'].update((nmr['port'].astype(str) + " " + nmr['name'].astype(str)).to_string(index=False))
          
            
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def Gobuster():

    sg.theme('DarkPurple6')

    layout = [
        
            
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("Gobuster")],
            [sg.Text("Enter commands and operations below!")],
            [sg.Text('GB:'), sg.Input(key='-GBIN-',size=(20,1))],
            [sg.Output(size=(100,30), key='-COUTPUT-')],
            [sg.Button("Send", key="-GBSEND-", bind_return_key=True)],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='Exit') ]
            
            
            ]
    window = sg.Window("Gobuster Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9)
    choice = None
    while True:
        event, values = window.read()
        if event == "-GBSEND-":
            try: 
                args = shlex.split(values['-GBIN-'])

                output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0] 
                print(output.decode('utf-8'))
            except:
                print("Error!")
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()



def Enumeration():

    sg.theme('DarkPurple6')

    layout = [
        
            
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("Enumeration")],
            [sg.Button("NMAP", button_color=('white', 'firebrick3'), key='-NMAP-')],
            [sg.Button("Gobuster", button_color=('white', 'firebrick3'), key='-GB-')],
            [sg.Button("Results", button_color=('white', 'firebrick3'), key='-RS-')],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='-EXIT-')]
            ]
    window = sg.Window("Enum Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9)
    choice = None
    while True:
        event, values = window.read()
        if event == "-NMAP-":
            NMAP()
        if event == "-GB-":
            Gobuster()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break

    window.close()


def PenHUB():

    sg.theme('DarkPurple6')

    layout = [
        
            
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("Penetration Testing")],
            [sg.Button("Enumeration", button_color=('white', 'firebrick3'), key='-ENUM-')],
            [sg.Button("Exploitation", button_color=('white', 'firebrick3'), key='-EXP-')],
            [sg.Button("Information Gathered", button_color=('white', 'firebrick3'), key='-EOUT-')],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='-EXIT-')]
            ]
    window = sg.Window("PEN Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9)
    choice = None
    while True:
        event, values = window.read()
        if event == "-ENUM-":
            Enumeration()
        if event == "-EXP-":
            break
        if event == "-EOUT-":
            EnumResults()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break

    window.close()

