
import subprocess
import PySimpleGUI as sg
import nmap
import pandas as ps
import os
import GUItraffic as Packets
import shlex
import Penetration as Pen

ninfo = open('nmapinfo.txt', 'r')

contents = ninfo.read()

ninfo.close()



def cli():

    sg.theme('DarkAmber')

    layout = [
        
            
            [sg.Text("Coyote", size=(40, 1), font=('Any 15'))],
            [sg.Text("CLI")],
            [sg.Text("Enter commands and operations below!")],
            [sg.Text('CLI:'), sg.Input(key='-CIN-',size=(20,1))],
            [sg.Output(size=(100,30), key='-COUTPUT-')],
            [sg.Button("Send", key="-CSEND-", bind_return_key=True)],
            [sg.Button("Exit", button_color=('white', 'firebrick3'), key='Exit') ]
            
            
            ]
    window = sg.Window("CLI Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9, font=('Courier'), resizable=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "-CSEND-":
            try: 
                args = shlex.split(values['-CIN-'])

                output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0] 
                print(output.decode('utf-8'))
            except:
                print("Error!")
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()



def main():

    ART = """    
                                            
                                    ░█████╗░░█████╗░██╗░░░██╗░█████╗░████████╗███████╗
                                    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝
                                    ██║░░╚═╝██║░░██║░╚████╔╝░██║░░██║░░░██║░░░█████╗░░
                                    ██║░░██╗██║░░██║░░╚██╔╝░░██║░░██║░░░██║░░░██╔══╝░░
                                    ╚█████╔╝╚█████╔╝░░░██║░░░╚█████╔╝░░░██║░░░███████╗
                                    ░╚════╝░░╚════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚══════╝
                                    
    
    """
    
    ART2 = """
    
    
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,@@@@,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@,,,,,,
,,,,,@@@@@@@@,,,,,,,,,,,,,,,,,,@@@@@@@@@,,,,,
,,,,,#@@@@@@@@@@@@*,,,,,,,,,,@@@@@@@@@@@@,,,,
,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,
,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,
,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,
,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,
,,,,,,,,,,,,,,,,,@@@,,,,,,,,@@@@@@@@@@@@@@@,,
,,,,,,,,,,,,,,,,,@@,,,,,,,,,,,,@@@@@@@@@@@@,,
,,,,,,,,,,,,,,,,@@@@,,,,,,,,,,,@@@@@@@@@@@@,,
,,,,,,,,,*,,,@@@@@@@@*,,,,,,,,,@@@@@@@@@@@,,,
,,,,,,,,,&@@@@@@@@@@@@@@@,,*,@@@@@@@@@@@@,,,,
,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,
,,,,,,,&@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,
,,,,,,,@@@@@@@@@@@@@@@@@@@@@@*,,,,,,,,,,,,,,,
,,,,,,,,,@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,@@@@/,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    
    
        """
    
    ART4 = """
,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,@@@@,,,,,,,,,@@@@,,,,,
,,,,,@@@@@@@@@@@@@@@@@@,,,,
,,,,,,@@@@@@@@@@@@@@@@@,,,,
,,,,,,,,,,,@,,,,@@@@@@@@,,,
,,,,,,,,,,@@,,,,,,@@@@@@,,,
,,,,,,,@@@@@@@@,,@@@@@@,,,,
,,,,,,@@@@@@@@@@@@@,,,,,,,,
,,,,,,,@@@@@@@,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,

    """

    ART3 = """

   .+------+     +------+     +------+     +------+     +------+.
 .' |    .'|    /|     /|     |      |     |\     |\    |`.    | `.
+---+--+'  |   +-+----+ |     +------+     | +----+-+   |  `+--+---+
|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
|  ,+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+   |
|.'    | .'    |/     |/      |      |      \|     \|    `. |   `. |
+------+'      +------+       +------+       +------+      `+------+
    """
    
    sg.theme('DarkAmber')

    
    layout = [
        
            [sg.Text(ART4), sg.Text(ART3), sg.Text(ART4)],
            [sg.Text(ART)],
            [sg.Text("Homepage")],
            [sg.Text("Menu WIP: Options below")],
            [sg.Button("Get Started", button_color=('white', 'firebrick3'), key='-GS-'), sg.Button("Penetration Testing", button_color=('white', 'firebrick3'), key='-PT-')],
            #[sg.Button("IPTracker", button_color=('white', 'firebrick3'), key='-IP-') ],
            [sg.Button("CLI", button_color=('white', 'firebrick3'), key='-CLI-') ],
            [sg.Button("Exit", key="-MENUEXIT-", button_color=('white', 'firebrick3'), pad=(250,0))]
          
            
            ]
    window = sg.Window("Main Menu", layout, icon=icon, grab_anywhere=True, font=('Courier'), resizable=True, auto_size_text=True)
    choice = None

    while True:
        event, values = window.read()


        if event == "-PT-":
            Pen.PenTest()
        if event == "-CLI-":
            cli()
            
        if event == "-MENUEXIT-" or event == sg.WIN_CLOSED:
            break
        
    window.close()

    
if __name__ == "__main__":
    icon = 'images/IMG-0886.PNG'
    main()
