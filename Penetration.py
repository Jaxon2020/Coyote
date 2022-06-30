



from pickle import FALSE
from random import weibullvariate
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








#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
def NMAP():

    sg.theme('DarkBlack')

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











#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
def PenTest():

    sg.theme('DarkBlack')

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


    ART4 = """
    

    
███████████████████████████████████
█─▄▄▄─█─▄▄─█▄─█─▄█─▄▄─█─▄─▄─█▄─▄▄─█
█─███▀█─██─██▄─▄██─██─███─████─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀
    
    
    
    
    """



    leftcol = [


        [sg.pin(sg.Text("Awaiting Data", key='-INFOTITLE-', visible=False, text_color='#0bff00')), sg.Push()],
        
        [sg.pin(sg.Text("Waiting for Data", key='-DC-', visible=False, text_color='#0bff00'))],
        
        

    ]

    rightcol = [
    
        [sg.Button("CLI", key='-CLI-', button_color=('#0bff00', 'Black')), sg.Button("NMAP", key="NMAP", button_color=('#0bff00', 'Black'))],
        [sg.Button('Output', key='OUTPUT', button_color=('#0bff00', 'Black')), sg.Button("Add Info", key='-ADEXINFO-', button_color=('#0bff00', 'Black'))],
        
    ]



    layout = [
        
            
            


            [sg.Text(ART4, text_color='#0bff00')],
            
            [sg.Button("Options: ", key='-OP-', button_color=('#0bff00', 'Black')), sg.pin(sg.Column(rightcol, visible=False, key="-OPC-")), sg.Push()],
            [sg.Column(leftcol, element_justification='c') ,sg.Text(ART, key='-ART-', text_color='#0bff00'), sg.pin(sg.Text("Waiting for Data", key='-WEB-', visible=False, text_color='#0bff00'))],
            [sg.Text("", key='-EXINFO-', visible=False)],
            [sg.pin(sg.Text("Add Info:", text_color='#0bff00', visible=False)),sg.pin(sg.Input(key='-INFOIN-', visible=False)),sg.pin(sg.Input('CLI', key='-CLIIN-', visible=False)), sg.pin(sg.Button('Submit', key='SUB', visible=False, button_color=('#0bff00', 'Black')))],
            [sg.pin(sg.Output(size=(40,15), key='-1OUT-', text_color='#0bff00', visible=False))],
            [sg.Button("Display", key="-ESEND-", bind_return_key=True, button_color=('#0bff00', 'Black'))],
            [sg.Button("Add to DB", key="-DBSEND-", visible=False, button_color=('#0bff00', 'Black'))],
            [sg.Button("Exit", button_color=('#0bff00', 'Black'), key='Exit', auto_size_button=True) ]
            
            
            ]
    window = sg.Window("Begin the Hunt", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', font=('Courier'), resizable=True, auto_size_text=True)
    choice = None


    opened1, opened2, opened3 = False, False, False

    while True:
        event, values = window.read()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
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
                  

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

        if event == '-ADEXINFO-':
            window['-EXINFO-'].update(values['-INFOIN-'], visible=True)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
        if event == "-CLI-":
            opened3 =  not opened3
            window['-CLIIN-'].update(visible=opened3)
            window['SUB'].update(visible=opened3)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

        if event == 'SUB':
            try: 
                args = shlex.split(values['-CLIIN-'])

                output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0] 
                print(output.decode('utf-8'))
            except:
                print("Error!")
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
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

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

        if event == 'OUTPUT':
            opened1 = not opened1
            window['-1OUT-'].update(visible=opened1)
          
                
   
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
        if event == '-OP-':
            opened2 = not opened2
            window['-OPC-'].update(visible=opened2)



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
        if event == 'NMAP':
            NMAP()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()









#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////DESCRIPTION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
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



