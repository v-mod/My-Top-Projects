from flask import Flask
import tello_controller
app = Flask(__name__)

@app.route('/')
def index():
    return 'Active'

@app.route('/api/execute/<command>')
def api_exec(command):
    tello_controller.execute(command)
    return 'EXEC-NO-FAIL'
