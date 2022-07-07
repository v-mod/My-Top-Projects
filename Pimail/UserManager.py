import os.path
class User:
    def __init__(self, userName, password, email, fname, lname, dob):
        self.userName = userName
        self.password = password
        self.email = email
        self.fname = fname
        self.lname = lname
        self.dob = dob

class UserManager:

    def Auth(self,userName,password):
        path = 'C:\\Users\\vivaa\\OneDrive\\Documents\\Coding\\Sys\\Users\\'
        if os.path.isfile(path + userName + '.txt'):
            f = open(path + userName + '.txt', 'r')
            data = f.read()
            userData = data.split(',')
            f.close()
            cpassword = userData[1]
            if cpassword == password:
                user = User(userData[0], '', userData[2], userData[3], userData[4], userData[5])
                return { 'user': user, 'message': 'User found' }
        else:
            return { 'user': None, 'message': 'No such user found' }