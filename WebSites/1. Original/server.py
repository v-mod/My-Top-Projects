from flask import Flask, render_template, request, redirect, url_for, flash, session
import UserManager as UM
import os
app = Flask(__name__)
app.secret_key='AAAAB3NzaC1yc2EAAAABJQAAAQEAvI+0heu2jKKSiaUEMTay7xsOhEOwapBsosHgo8jFbiELcXB1gwtELKmiLdkFRoowBb2Ga1VRJVtgeLtetM4FYu7xbRtoQB/E3tbnAJbiMy4pUCGMeI2lIFTFL0vWHGsqH/5qdoXu0dFijfdyxqvj/F5SZH7vpIXNZJu9Nvsr4UEnDWl16ndcVHsel1aMdW93I2OGLpEf8yvMR+Lq7ugVldUu2dC3FJMbZ4OkQiafDqA4ulLKk1SFRC0SsFlhIm/7XZVua4ckxEYdFRAn5NIC76ARyQUBANhIHhGkdApHm4m6ykhtozEPVagjIsNtuaZKFqOESL3ltIotHIHar/HL4Q'
userManager = UM.UserManager()
userInfo = None
userName=None
@app.route('/')
def homepage():
    if 'UserId' in session:
        userId = session['UserId']
        return render_template('home.html', userId=userId)
    else:
        userId= ''
        return render_template('home.html', userId=userId)
@app.route('/help')
def help_page():
    if 'UserId' in session:
        userId = session['UserId']
        return render_template('help.html', userId=userId)
    else:
        userId= ''
        return render_template('help.html', userId=userId)
@app.route('/profile/me')
def profile_page():
    if 'UserId' in session:
        userId = session['UserId']
        return render_template('profile.html', userId=userId)
    else:
        return redirect(url_for('homepage'))
@app.route('/login')
@app.route('/auth/login')
def login():
    return render_template('login.html')
@app.route('/logout')
@app.route('/auth/logout')
def logout():
    userInfo=None
    session.pop('UserId', None)
    return render_template('logout.html')
@app.route('/service/auth', methods=['POST'])
def auth_service():
    UserId = request.form['uname']
    Pwd = request.form['psw']
    print(UserId,Pwd)
    res = userManager.Auth(UserId, Pwd)
    userInfo = res['user'] 
    if userInfo != None:    
        userName=UserId
        session['UserId'] = UserId
        flash('Logged in successfully.')
        return redirect(url_for('homepage'))        
    else:
        flash('Incorrect Password')
        return redirect(url_for('login'))
@app.route('/clip/<clipId>')
def clip(clipId):
    if os.path.isfile("clips\\"+clipId+".clip"):
        if'UserId' in session:
            f=open('clips\\'+clipId+'.clip', 'r')
            clipData=f.read()
            userId = session['UserId']
            f.close()
            return render_template('clipboard.html',clipId=clipId, userId=userId, clipData=clipData)
        else:
            return redirect(url_for('login'))
    else:
        if'UserId' in session:
            f=open('clips\\'+clipId+'.clip', 'x')
            clipData=''
            userId = session['UserId']
            f.close()
            return render_template('clipboard.html',clipId=clipId, userId=userId, clipData=clipData)
        else:
            return redirect(url_for('login'))

@app.route('/service/clip', methods=['POST'])
def clip_service():
    clipId=request.form['clipId']
    clipData = request.form['clipData']
    f = open("clips\\"+clipId+".clip", "w")
    f.write(clipData)
    f.close()
    return redirect('/')  
@app.route('/access_clip')
def access_clip():
    return render_template('access_clip.html')
if __name__ == '__main__':
    app.run(debug=False)
