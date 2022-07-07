import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess
import requests
from ecapture import ecapture as ec
import random
import win32api
from pynput.keyboard import Key,Controller
import smtplib
import ctypes   
import datetime 
import pychromecast
keyboard=Controller()
def speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[0].id')
    engine.say(text)
    engine.runAndWait()
def open_in_browser(addr):
    return webbrowser.open_new_tab(addr)
def take_a_photo():
    return ec.capture(0,"camera",'img'+str(random.randint(1,99999999999))+'.jpg')
def open_app(statement):
    return os.system('start'+statement+':')
def play_pause():
    VK_MEDIA_PLAY_PAUSE = 0xB3
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)
def volume_up():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)
    return speak('Ok, increasing the volume')
def volume_down():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)
    return speak('Ok, decreasing the volume')
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-gb')
            print(f'<-t: {statement}\n')

        except Exception as e:
            speak("Pardon me, please say that again")
            return takeCommand()
        return statement
def check():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source,phrase_time_limit=1)
        try:
            statement=r.recognize_google(audio,language='en-gb')
        except Exception as e:
            return "None"
        return statement
def lock():
    ctypes.windll.user32.LockWorkStation()