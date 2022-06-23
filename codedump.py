import PySimpleGUI as sg

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
    window = sg.Window("Enum Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9)
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
    window = sg.Window("PEN Window", layout, icon='images/Coyote.ico', grab_anywhere=True, element_justification='c', alpha_channel=.9)
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