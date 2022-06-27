


import subprocess
import PySimpleGUI as sg
import nmap
import pandas as ps
import os
import GUItraffic as Packets
import shlex
import sqlite3 as sql


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
    window = sg.Window("Main Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9)
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
                
                
                print( "\n", test_data[['protocol', 'port', 'name','version', 'state', 'reason' ]])
            except:
                print("Error!")
            

    window.close()


def PenTest():

    sg.theme('DarkPurple6')

    ART = """
    
     .=====.. |==|
    ||     || |= |
 _  ||     || |^*| _
|=| o=,===,=o |__||=|
|_|  _______)~`)  |_|
    [=======]  ()    
    
    
        """



    ART2 = """
   
           .=====.. |==|
          ||     || |= |
       _  ||     || |^*| _
<=====|=| o=,===,=o |__||=|
      |_|  _______)~`)  |_|
          [=======]  ()    
                

            """




    ART3 = """

           .=====.. |==|
          ||     || |= |
       _  ||     || |^*| _
<=====|=| o=,===,=o |__||=|=====>
      |_|  _______)~`)  |_|
          [=======]  ()    
                
            """



    leftcol = [


        [sg.pin(sg.Text("Awaiting Data", key='-INFOTITLE-', visible=False)), sg.Push()],
        
        [sg.pin(sg.Text("Waiting for Data", key='-DC-', visible=False))],
        
        

    ]

    layout = [
        
            
            


            [sg.Text("Coyote")],
            [sg.Column(leftcol, element_justification='c') ,sg.Text(ART, key='-ART-'), sg.pin(sg.Text("Waiting for Data", key='-WEB-', visible=False))],
            [sg.Text("", key='-EXINFO-', visible=False)],
            [sg.Text("Add Info:"),sg.Input(key='-INFOIN-'),sg.Button("Add Info", key='-ADEXINFO-'), sg.Button("NMAP", key="NMAP")],
            [sg.Text("CLI:"),sg.Input(key='-IN-'),sg.Button("Intiate CLI", key='-CLI-')],
            [sg.Output(size=(40,15), key='-1OUT-')],
            [sg.Button("Display", key="-ESEND-", bind_return_key=True)],
            [sg.Button("Add to DB", key="-DBSEND-")],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='Exit') ]
            
            
            ]
    window = sg.Window("Results Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9, font=('Courier'), resizable=True, auto_size_text=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "-ESEND-":
            
            webr = 0
            nmr = ps.read_csv('nmapdump.csv', sep = ';', header = 0)
            if nmr.empty:
                print("No data to display")
            elif(webr == 0):
                window['-ART-'].update(ART2)
                window['-DC-'].update((nmr['protocol'].astype(str) + " " + nmr['port'].astype(str) + " " + nmr['name'].astype(str)).to_string(index=False), visible=True)
                #window['-WEB-'].update((nmr['port'].astype(str) + " " + nmr['name'].astype(str)).to_string(index=False), visible=True)
                window['-INFOTITLE-'].update(("Host:" + " " + nmr['host'][0] + "(" + nmr['hostname'][0] + ")"),visible=True)
            else:
                  window['-ART-'].update(ART3)
                  window['-DC-'].update((nmr['protocol'].astype(str) + " " + nmr['port'].astype(str) + " " + nmr['name'].astype(str)).to_string(index=False), visible=True)
                  window['-INFOTITLE-'].update(("Host:" + " " + nmr['host'][0] + "(" + nmr['hostname'][0] + ")"),visible=True)
        if event == '-ADEXINFO-':
            window['-EXINFO-'].update(values['-INFOIN-'], visible=True)
        if event == "-CLI-":
            try: 
                args = shlex.split(values['-IN-'])

                output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0] 
                print(output.decode('utf-8'))
            except:
                print("Error!")
        if event == "-DBSEND-":

            con = sql.connect("Coyote.db")

            cursor = con.cursor()
       
            if os.path.exists("Coyote.db"):
                print("Using Coyote.db")
            else:
                print("The file does not exist")
                cursor.execute("CREATE TABLE nmap (host TEXT, protocol TEXT, port INT, name TEXT, state TEXT, product TEXT, extrainfo TEXT, reason TEXT, version TEXT)")


            nmr = ps.read_csv('nmapdump.csv', sep = ';', header = 0)
            nmaprows = []
            for i in nmr.index:
                nmaprows = [nmr['host'][i], nmr['protocol'][i], (nmr['port'][i]), nmr['name'][i],nmr['state'][i],nmr['product'][i],nmr['extrainfo'][i],nmr['reason'][i],nmr['version'][i]]
                sql_command = 'INSERT INTO nmap VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                cursor.execute(sql_command, nmaprows)
            
           
            con.commit()
            rows = cursor.execute("SELECT host, protocol, port, name, state, product, extrainfo, reason, version FROM nmap").fetchall()

            print(rows)

        if event == 'NMAP':
            NMAP()

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
    window = sg.Window("Gobuster Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9)
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



