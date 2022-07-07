import AriaAI
import datetime
import os
import RPi.GPIO as GPIO
import time
import pixelController
import requests
import json
pixels = pixelController.Pixels()
Aria_API_KEY='011'
Aria_API_URL='https://irisassist.azurewebsites.net/aria/api/ask/'
def start_up():
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('__   ___    __    _______ ')
    print('| |  ||\\   | |   /  ____|')
    print('| |  ||_// | |   |  |___  ')
    print('| |  || \\  | |   |____  |')
    print('|_|  ||  \\ |_|   |______|')
    print('')
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
    print('Made by Vivaan')
    print('Born in March 2021')
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
        Aria('Aria')
    else:
        print('Unkown Command')
#    elif 'email' in cmd:
#        to = input('To: ')
#        content = input('Content: ')
#        sendEmail(to,content)
def Aria(assist_name):
    BUTTON = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)
    while True:
        state = GPIO.input(BUTTON)
        if not state:
            request()
        time.sleep(0.1)
def request():
    AriaAI.speak("How can I help?")
    time.sleep(2)
    print("Listening...")
    statement = AriaAI.takeCommand().lower()
    pixels.think()
    time.sleep(2)
    Aria_API_COMPLETE_URL=Aria_API_URL+Aria_API_KEY+'/'+statement
    r=requests.get(Aria_API_COMPLETE_URL,verify=False).text
    print(r)
    result=r.split('_')
    if result[0] == '' and result[1] == '':
        AriaAI.speak("Sorry, I don't know how to help with that")
    elif result[0] == '':
        AriaAI.speak(result[1])
    else:
        AriaAI.speak("Sorry, I don't know how to help with that")
