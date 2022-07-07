import Chat
import UserManager as UM
import Cmd
path = 'C:\\Users\\vivaa\\OneDrive\\Documents\\Coding\\Sys'
userManager = UM.UserManager()
Version = 'V2.5'
print('Hello and welcome to Pios ',Version)
userName = input('Username: ')
password = input('Password: ')
result = userManager.Auth(userName, password)
user =  result['user']
if user == None:
    print(result['message'])
else:
    Cmd.mainInterface(userName,password,path)