import PySimpleGUI as sg
import nmap



def main():

    sg.theme('DarkPurple6')

    layout = [
                [sg.Text('NMAP: Network Mapper'), sg.Button("Open Cheat Sheet", key="open")],
                [sg.Text('IP:'), sg.Input(key='-IP-',size=(20,1)), sg.Text('Test'), sg.Input(key='-ARGS-', size=(20,1))],
                [sg.Output(size=(100,50), key='-OUTPUT-')],
                [sg.Button("Send", key="-SEND-")],

            
                ]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            if sg.Window("Other Window", [[sg.Text("Cheat Sheet")], 
                                          [sg.Text("Commonly used NMAP Options: ")], 
                                          [sg.Text("-A: Enable OS detection, version detection, script scanning, and traceroute")], 
                                          [sg.Yes(), sg.No()]]).read(close=True)[0] == "Yes":
                print("User chose yes!")
            else:
                print("User chose no!")
        if event == "-SEND-":
            print("Starting NMAP scan! This may take some time!")
            nm = nmap.PortScanner()
            nm.scan(hosts=values['-IP-'], anmarguments=values['-ARGS-'])
            print(nm[values['-IP-']].hostname())
            print(nm[values['-IP-']].all_tcp())
            print(nm.scaninfo())
        
    window.close()



    
if __name__ == "__main__":
    main()
