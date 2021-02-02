import PySimpleGUI as sg
f = True
while f == True:
    word = 'welcome'
    layout = [
        [sg.Text('The word is: hfhorzp')],
        [sg.Text('Find the right cipher and unscramble the word')],
        [sg.Text('Word:', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Puzzle', layout)
    event, values = window.read()
    if values[0] not in word:
        print("Incorrect!")
        exit()
    elif values[0] in word:
        print("Correct!")
        f = False
