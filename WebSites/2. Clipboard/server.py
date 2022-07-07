from flask import Flask, render_template, request, redirect, url_for, flash, session
import UserManager as UM
from Clipboard.model.Clip import Clip
from Clipboard.services.ClipService import ClipService

import os
from Helper import AuthCheck
app = Flask(__name__)
app.secret_key='AAAAB3NzaC1yc2EAAAABJQAAAQEAvI+0heuc2jKKSiaUEMTay7xsOhEOwapBsosHgo8jFbiELcXB1gwtELKmiLdkFRoowBb2Ga1VRJVtgeLtetM4FYu7xbRtoQB/E3tbnAJbiMy4pUCGMeI2lIFTFL0vWHGsqH/5qdoXu0dFijfdyxqvj/F5SZH7vpIXNZJu9Nvsr4UEnDWl16ndcVHsel1aMdW93I2OGLpEf8yvMR+Lq7ugVldUu2dC3FJMbZ4OkQiafDqA4ulLKk1SFRC0SsFlhIm/7XZVua4ckxEYdFRAn5NIC76ARyQUBANhIHhGkdApHm4m6ykhtozEPVagjIsNtuaZKFqOESL3ltIotHIHar/HL4Q'
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
    AuthCheck()
    userId = session['UserId']
    clipService = ClipService()
    clip = clipService.get(clipId)
    if clip != None and (clip.visibility == 'public' or clip.owner == userId):
        return render_template('clipboard.html',clip=clip, userId = session['UserId'])
    elif clip == None:
        return render_template('clipboard.html',clip= Clip(clipId, None, 'private','' ), userId = session['UserId'])
    else:
        return render_template('access_denied.html')

@app.route('/service/clip', methods=['POST'])
def clip_service():
    clipId=request.form['clipId']
    clipData = request.form['clipData']
    visibility=request.form['visibility']
    userId = session['UserId']
    clipService = ClipService()
    clip = Clip(clipId, None, visibility, clipData)
    result = clipService.set(clip, userId)
    if result == 'successful_save':
        return redirect('/')
    elif result == 'access_denied':
        return render_template(result+'.html')
    else:
        return render_template('server_fatal_error.html', errorId='MALFUNC_SET_CLIP')
@app.route('/access_clip')
def access_clip():
    return render_template('access_clip.html')
@app.route('/auth/signup')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/service/signup', methods=['POST'])
def signup_service():
    userName=request.form['userName']
    password=request.form['pwd']
    fname=request.form['fname']
    lname=request.form['lname']
    dob=request.form['dob']
    email=request.form['email']
    userManager.Signup(userName, password, email, fname, lname, dob)
    return redirect('/auth/login')
if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')