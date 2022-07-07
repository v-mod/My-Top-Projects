import AriaCoreTools
Aria=AriaCoreTools.Aria
AriaAI=AriaCoreTools.AriaAI
Thread=AriaCoreTools.threading.Thread
if __name__=='__main__':
    f = open('C:/Aria/user.txt')
    name=f.read()
    f.close()
    Aria.start_up()
    Aria.sayHi(name)
    AriaListen = Thread(target=Aria.Aria)
    AriaListen.start()