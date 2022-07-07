class MainInterface:
    def __init__(self,user,chatStore):
        self.user = user
        self.chatStore = chatStore

    def ShowMMenu(self):
        while True:
            op=input('Email or Chat? ')
            if op == 'chat':
                op=input('Read [R] or Write [W] Message: ')
                if op == 'W' or op == 'w':
                   self.WriteMsg()
                if op == 'R' or op == 'r' :
                    self.ReadMsg()
            if op == 'email':
                op=input('Read [R] or Write [W] Email: ')
                if op == 'W' or op == 'w':
                   self.WriteEmail()
                if op == 'R' or op == 'r' :
                    self.ReadEmail()
    def WriteMsg(self):
        rcpt= input('To who: ')
        msg = input('Message: ')
        self.chatStore.StoreMsg(rcpt,msg,self.user.userName)
    def ReadMsg(self):
        data = self.chatStore.ReadMsg(self.user.userName)
        print(data)
    def WriteEmail(self):
        to=input('To(Email): ')
        cc=input('CC: ')
        bcc=input('BCC: ')
        sub=input('Subject: ')
        ct=input('Content: ')
        self.chatStore.StoreEmail(to,ct,cc,bcc,sub,self,self.user)
    def ReadEmail(self):
        data = self.chatStore.ReadMsg(self.user)
        print(data)