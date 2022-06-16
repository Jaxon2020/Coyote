
import subprocess
import PySimpleGUI as sg
import nmap
import pandas as ps
import os


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


def cli():

    sg.theme('DarkAmber')

    layout = [
        
            
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("CLI")],
            [sg.Text("Enter commands and operations below!")],
            [sg.Text('CLI:'), sg.Input(key='-CIN-',size=(20,1))],
            [sg.Output(size=(100,30), key='-COUTPUT-')],
            [sg.Button("Send", key="-CSEND-")],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='Exit') ]
            
            
            ]
    window = sg.Window("CLI Window", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, element_justification='c', alpha_channel=.9)
    choice = None
    while True:
        event, values = window.read()
        if event == "-CSEND-":
            try: 
                result = subprocess.check_output(values['-CIN-'])
                result = result.decode("utf-8")
                print(result)
            except:
                print("Error!")
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()



def main():
    
    sg.theme('DarkAmber')

    menu_def = [['File', ['Open', 'Save',]],
            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
            ['Help', 'About...'],]

    layout = [
        
            [sg.Button("Exit", key="-MENUEXIT-", button_color=('white', 'firebrick3'), pad=(190,0),  )],
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("Homepage")],
            [sg.Text("Menu WIP: Options below")],
            [sg.Button("NMAP", button_color=('white', 'firebrick3'), key='-NMAP-') ],
            [sg.Button("CLI", button_color=('white', 'firebrick3'), key='-CLI-') ]
          
            
            ]
    window = sg.Window("Main Menu", layout, icon='images/Coyote.ico', no_titlebar=True, grab_anywhere=True, alpha_channel=.9, size=(500,300))
    choice = None

    while True:
        event, values = window.read()
        if event == "-NMAP-":
            NMAP()
            
        if event == "-CLI-":
            cli()
            
        if event == "-MENUEXIT-" or event == sg.WIN_CLOSED:
            break
        
    window.close()

    
if __name__ == "__main__":
    main()
