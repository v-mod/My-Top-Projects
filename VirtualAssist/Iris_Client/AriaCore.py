import AriaAI
import datetime
import os
import playsound
import requests
import threading
import time
Aria_API_KEY='011'
Aria_API_URL=''
#    print('__   ___    __    _______ ')
#    print('| |  ||\\   | |   /  ____|')
#    print('| |  ||_// | |   |  |___  ')
#    print('| |  || \\  | |   |____  |')
#    print('|_|  ||  \\ |_|   |______|')
def execute(r,s):
    result=r.split('_')
    Part1=result[0]
    Part2=result[1]
    if result[0] == '' and result[1] == '':
        AriaAI.speak("Sorry, I don't know how to help with that")
    elif result[0] == '':
        AriaAI.speak(result[1])
    elif 'web.open' in result[0]:
        webURL=result[0].split('-')
        AriaAI.speak(Part2)
        AriaAI.open_in_browser(webURL[1])
    elif Part1 == 'photo-take':
        AriaAI.take_a_photo()
    elif Part1 == 'exit':
        quit()
    elif '.open'in Part1:
        appSplit=Part1.split('.')
        AriaAI.open_app(appSplit[0])
    else:
        AriaAI.speak("Sorry, I don't know how to help with that")
def start_up():
    try:
        requests.get('https://g.co')
        show_nolite()
    except:
        print('Hmm, I cant seem to connect to the internet.\n Switching to lite mode!')
        print('')
        show_lite()
def show_nolite():
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('     _         _       ')
    print('    / \   _ __(_) __ _ ')
    print("   / _ \ | '__| |/ _` |")
    print('  / ___ \| |  | | (_| |')
    print(' /_/   \_\_|  |_|\__,_|')
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('')
    print('Booting up Aria')
    print('')
    print('Hi, I am Aria')
    print('')
    print('I am now operational')
    print('Say "Aria" to activate me')
    print('Ask me "help" to see what i can do')
    print('Made by Vivaan Modi')
    print('Born in March 2021')
    print('')
    print('© Vivaan Modi 2021')
def show_lite():
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('     _         _         _ _ _')
    print('    / \   _ __(_) __ _  | (_) |_ ___')
    print("   / _ \ | '__| |/ _` | | | | __/ _ \ ")
    print('  / ___ \| |  | | (_| | | | | ||  __/')
    print(' /_/   \_\_|  |_|\__,_| |_|_|\__\___|')
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('')
    print('Booting up Aria')
    print('')
    print('Hi, I am Aria')
    print('')
    print('I am now operational')
    print('Say "Aria" to activate me')
    print('Ask me "help" to see what i can do')
    print('Made by Vivaan Modi')
    print('Born in March 2021')
    print('')
    print('© Vivaan Modi 2021')    
def sayHi(name):
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        AriaAI.speak("Hello,Good Morning" + name)
    elif hour>=12 and hour<18:
        AriaAI.speak("Hello,Good Afternoon" + name)
    else:
        AriaAI.speak("Hello,Good Evening" + name)
def cmd():
    cmd = input('(·_·) <- ')
    if 'assist' in cmd:
        Aria()
    else:
        print('Unkown Command')
#    elif 'email' in cmd:
#        to = input('To: ')
#        content = input('Content: ')
#        sendEmail(to,content)
def Aria():
    assist_name='aria'
    print('Starting keyword service...')
    time.sleep(1)
    print('Keyword Serice is on. \nAria is now listening to you!')
    while True:
        wask = AriaAI.check()
        if assist_name in wask:
            AriaRequest = threading.Thread(target=request)
            AriaRequest.start()
def request():
    AriaAI.speak("How can I help?")
    print("Listening...")
    statement = AriaAI.takeCommand().lower()
    Aria_API_COMPLETE_URL=Aria_API_URL+Aria_API_KEY+'/'+statement
    r=requests.get(Aria_API_COMPLETE_URL,verify=False).text
    print(r)
    execute(r,'_')