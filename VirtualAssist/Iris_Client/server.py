import main
from threading import Thread
from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
AriaThread = Thread(target=main.main)
AriaThread.start()

@app.route('/')
def index():
    return render_template('Aria.html')

@app.route('/mic/on')
def mic_on():
    session['mic'] = 'on'
    return 'Mic set to on'

@app.route('/mic/off')
def mic_off():
    session['mic'] = 'off'
    return 'Mic set to off'

@app.route('/screen')
def screen():
    return render_template('screen.html', mic=session['mic'])

if __name__ == '__main__':
    app.run()