import UserManager as UM
import ChatInterface as CI
import ChatStore as CS
import getpass
def software(userName, password):
    path = 'C:\\Users\\vivaa\\OneDrive\\Documents\\Coding\\Python\\Sys'
    userManager = UM.UserManager()
    Version = 'V2.5'
    print('Hello and welcome to Pimail ',Version)
    result = userManager.Auth(userName, password)
    user =  result['user']
    chatStore = CS.Store(path)
    chatInterface = CI.MainInterface(user,chatStore)
    chatInterface.ShowMMenu()