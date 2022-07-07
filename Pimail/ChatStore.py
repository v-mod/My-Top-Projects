import os.path
import time
class Store:
    def __init__ (self,path):
        self.path = path

    def StoreMsg(self,rcpt,msg,sdr):
        tm = time.asctime()
        f = open(self.path + '\\Messages\\' + rcpt + '.txt', 'a')
        data = tm + ': ' + sdr + ': ' + msg + '\n'
        f.write(data)
        f.close()
    def ReadMsg(self,userName):
        if os.path.isfile(self.path + '//Messages//' + userName + '.txt'):
            f = open(self.path + '//Messages//' + userName + '.txt', 'r')
            data = f.read()
            return data
    def StoreEmail(self,to,ct,cc,bcc,sub,user,email):
        tm = time.asctime()
        data = 'Dear ' + to + '\n' + 'CC: ' + cc + '\n' + 'BCC:' + bcc + '\n' + sub + '\n' + ct
        f = open(self.path + '//Emails//' + to + '.txt', 'a')
        f.write(data)
        f.close()
        f = open(self.path + '//Emails//' + cc + '.txt', 'a')
        f.write(data)
        f.close()
        f = open(self.path + '//Emails//' + bcc + '.txt', 'a')
        f.write(data)
        f.close()
    def ReadEmail(self,user):
        f = open(self.path + '//Emails//' + user.email + '.txt', 'r')
        data = f.read()
        f.close()
        return data


