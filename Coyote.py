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


ART4 = """
    

    
███████████████████████████████████
█─▄▄▄─█─▄▄─█▄─█─▄█─▄▄─█─▄─▄─█▄─▄▄─█
█─███▀█─██─██▄─▄██─██─███─████─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀
    
    
    
    
    """



def cli():

    sg.theme('DarkBlack')

    layout = [
        
            
            [sg.Text(ART4, text_color='#0bff00' )],
            [sg.Text("CLI",text_color='#0bff00')],
            [sg.Text("Enter commands and operations below!", text_color='#0bff00')],
            [sg.Text('CLI:',text_color='#0bff00'), sg.Input(key='-CIN-',size=(20,1))],
            [sg.Output(size=(100,30), key='-COUTPUT-')],
            [sg.Button("Send", key="-CSEND-", bind_return_key=True, button_color=('#0bff00', 'Black'))],
            [sg.Button("Exit", button_color=('#0bff00', 'Black'), key='Exit') ]
            
            
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
    ,,,,,,,,,,,,,,,,,,,
    ,@@@@,,,,,,,,,@@@@,,
    ,@@@@@@@@@@@@@@@@@@,,
    ,,@@@@@@@@@@@@@@@@@,,
     ,,,,,,@,,,,@@@@@@@@,
     ,,,,,@@,,,,,,@@@@@@,
    ,,,@@@@@@@@,,@@@@@@,,
    ,,@@@@@@@@@@@@@,,,,,
    ,,,@@@@@@@,,,,,,
      ,,,,,,,,,

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
        
            [sg.Text(ART4, text_color='#0bff00',background_color='black'), sg.Text(ART3, text_color='#0bff00',background_color='black'), sg.Text(ART4, text_color='#0bff00',background_color='black')],
            [sg.Text(ART, text_color='#0bff00',background_color='black')],
            [sg.Button("Begin the Hunt", button_color=('#0bff00', 'Black'), key='-PT-')],
            [sg.Button("CLI", button_color=('#0bff00', 'Black'), key='-CLI-'), sg.Button("NMAP", button_color=('#0bff00', 'Black'), key='NMAP') ],
            [sg.Button("Exit", key="-MENUEXIT-", button_color=('#0bff00', 'Black'), pad=(250,0))]
          
            
            ]
    window = sg.Window("Main Menu", layout, icon=icon, grab_anywhere=True, font=('Courier'), resizable=True, auto_size_text=True, background_color='black')
    choice = None

    while True:
        event, values = window.read()


        if event == "-PT-":
            Pen.PenTest()
        if event == "-CLI-":
            cli()
        if event == 'NMAP':
            Pen.NMAP()
        if event == "-MENUEXIT-" or event == sg.WIN_CLOSED:
            break
        
    window.close()

    
if __name__ == "__main__":
    icon = 'images/IMG-0886.PNG'
    main()
