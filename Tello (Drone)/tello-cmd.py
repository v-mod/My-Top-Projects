from tello import Tello
import sys
from datetime import datetime
import time

tello = Tello()

start_time = str(datetime.now())

command='command'
tello.send_command(command.rstrip())
command=''

while True:
    command=input('tello@TELLO-FE02B7: ~ $ ')
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

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
