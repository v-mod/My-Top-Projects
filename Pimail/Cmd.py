import os.path
import Chat
import Adminos as Admin
import time
def mainInterface(userName,password,path):
    cmd_run = userName + '@pios: '
    cmd = input (cmd_run)
    userName
    cmdFO(userName, password,cmd,path)
def cmdFO(userName, password,cmd,path):
    if cmd == 'software.chat':
        Chat.software(userName, password)
    if cmd == 'admin.chat':

    else:
        print('Command not found')
        mainInterface(userName,password,path)