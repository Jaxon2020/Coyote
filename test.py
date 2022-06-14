import PySimpleGUI as sg
import nmap



def main():

    sg.theme('DarkPurple6')

    layout = [
                [sg.Text('NMAP: Network Mapper')],
                [sg.Text('IP:'), sg.Input(key='-IP-',size=(20,1)), sg.Text('Test'), sg.Input(key='-ARGS-', size=(20,1))],
                [sg.Output(size=(100,50), key='-OUTPUT-')],
                [sg.Button("Send", key="-SEND-")],

            
                ]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-SEND-":
            print("Starting NMAP scan! This may take some time!")
            nm = nmap.PortScanner()
            nm.scan(hosts=values['-IP-'], arguments=values['-ARGS-'])
            print(nm[values['-IP-']].hostname())
            print(nm[values['-IP-']].all_tcp())
            print(nm.scaninfo())
        
    window.close()



    
if __name__ == "__main__":
    main()
