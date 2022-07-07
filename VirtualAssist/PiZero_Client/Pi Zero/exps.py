import PySimpleGUI as sg
sg.theme('DarkPurple')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('PyDa', layout)
event, values = window.read()
print(event)
print(values)
print(values[0])