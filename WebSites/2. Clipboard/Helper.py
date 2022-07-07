from flask import redirect, url_for, session

def AuthCheck():
    if 'UserId' not in session:
        return redirect(url_for('login'))