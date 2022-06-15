

import PySimpleGUI as sg
import nmap
import pandas as ps
import os


ninfo = open('nmapinfo.txt', 'r')

contents = ninfo.read()

ninfo.close()

def make_win1():
    layout = [[sg.Text('This is the FIRST WINDOW'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Text('Click Popup anytime to see a modal popup')],
              [sg.Button('Launch 2nd Window'), sg.Button('Popup'), sg.Button('Exit')]]
    return sg.Window('Window Title', layout, location=(800,600), finalize=True)


def main():

    sg.theme('DarkPurple6')

    layout = [
                [sg.Text('NMAP: Network Mapper'), sg.Button("Open Cheat Sheet", key="open")],
                [sg.Text('IP:'), sg.Input(key='-IP-',size=(20,1)), sg.Text('Options'), sg.Input(key='-ARGS-', size=(20,1))],
                [sg.Output(size=(100,30), key='-OUTPUT-')],
                [sg.Button("Send", key="-SEND-")],

            
                ]
    window1, window2 = sg.Window("Main Window", layout), None
    while True:
        event, values = window1.read()
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
            
            print(test_data)

    window.close()



    
if __name__ == "__main__":
    main()
