import os 
import shutil
import getpass
import requests
from pathlib import Path
from pyshortcuts import make_shortcut
print('Hi and welcome to the Iris setup wizard.')
print('To begin with, please login...')
user=input('Email: ')
pwd=getpass.getpass('Password: ')
print('Ok, authenticating...')
r=requests.get('https://xlick.pythonanywhere.com/Aria/api/user/'+user+'/'+pwd)
if user == 'admin':
    if pwd == 'Wastes123':
        print('Hello Admin.')
    else:
        print('YOU ARE NOT ADMIN!!!')
        quit()
elif r.text == 'User not found':
    print('Invlid Credentials')
    exit()
else:
    print('Hello, '+user+'. Time to start')
print('Aria is only compatible with python version 3.6. Please note that you will need to modify your python setup to enable envirment variables if you have not already.')
v = input('Have you installed a compatible version (y/n)? If you are unsure about your version the say y and it will fail if you have an incorrect version. ')
if v == 'y':
    print('Great, now lets begin setup.')
else:
    print('Downloading python installer')
    os.system('cd C:/Aria/installation && curl https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe > python3.6.exe')
    os.system('cd C:/Aria/installation && python3.6.exe')
print('Creating neccesary folders')
os.system('cd C:/ && mkdir Aria')
os.system('cd C:/Aria && mkdir installation ')
os.system('cd C:/Aria/installation')
print('Donwnloading Installation Files')
os.system('cd C:/Aria && curl https://xlick.pythonanywhere.com/static/aria.ico')
os.system('cd C:/Aria/installation && curl https://xlick.pythonanywhere.com/static/requirements.txt > requirements.txt')
print('Great, now lets install the dependencies')
os.system('pip install -r C:/Aria/installation/requirements.txt')
print('Ok, now lets download the app.')
os.system('cd C:/Aria/installation && curl https://xlick.pythonanywhere.com/static/Iris_Client.zip ')
os.system('cd C:/Aria/installation && powershell.exe Expand-Archive -Path Iris_Client.zip -DestinationPath C:/Aria')
name=input('What would you like to be called?: ')
os.system('cd C:/Aria && echo '+name+'  > user.txt')
print('Creating Shortcuts...')
#make_shortcut('C:/Aria/core/server.py', name='Aria',
#                        icon='C:/Aria/iris.ico',description='Aria')
print('installation complete!')