from tello import Tello
import sys
from datetime import datetime
import time

tello = Tello()

def execute(command):
    if command != '' and command != '\n':
        command = command.rstrip()
        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        elif command == 'exit':
            quit()
        if command == 'em':
            tello.send_command('emergency')
        else:
            tello.send_command(command)

def connect_sdk():
    execute('command')

def takeoff():
    execute('takeoff')

def land():
    execute('land')

def forward(x):
    execute('forward '+x)

def back(x):
    execute('back '+x)

def left(x):
    execute('left '+x)

def right(x):
    execute('right '+x)

def flip(d):
    execute('flip '+d)

def rotate_clockwise(x):
    execute('cw '+x)

def rotate_counter_clockwise(x):
    execute('ccw '+x)

def stop():
    execute('stop')

def emergency():
    execute('em')

start_time = str(datetime.now())
