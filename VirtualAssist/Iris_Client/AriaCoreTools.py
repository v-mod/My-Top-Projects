try:
    import main
    import threading
    import requests
    import speech_recognition as sr
    import pyttsx3
    import webbrowser
    import os
    import subprocess
    from ecapture import ecapture as ec
    import random
    import win32api
    from pynput.keyboard import Key,Controller
    import smtplib
    import ctypes   
    import datetime 
    import pychromecast
    import AriaAI
    import AriaCore
    requests=requests
    Aria=AriaCore
    AriaAI=AriaAI
    Core=main
    threading=threading
    def get(url):
        return requests.get(url)
    def post(url):
        return requests.post(url)
except ImportError:
    print('WARNING: IMPORT ERROR. IT IS RECOMENDED YOU INSTALL')
    install=input('Install [Y/n]: ')
    if install.lower == 'y':
        import AriaInstaller
        AriaInstaller.install()
    else:
        print('Ok, cancelling installation and quiting')
        quit()
def write(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()
    return 'Data written'
def read(file):
    f=open(file)
    data = f.read()
    f.close()
    return data
def help():
    print('This is Arias Core Tools module. It groups everything together!')
