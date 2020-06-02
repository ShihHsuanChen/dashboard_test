import time
import json
import requests
import traceback
from random import randint
from datetime import datetime
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit


""" service settine """
HOST = '127.0.0.1'
PORT = '5003'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!#$%^DSDS'
print(app.template_folder)
socketio = SocketIO(app)


def parse_reqdata(req):
    content_type = req.headers['content-type']
    try:
        if 'application/json' in content_type:
            data = req.json
        elif 'application/x-www-form-urlencoded' in content_type:
            data = req.form.to_dict()
        elif 'multipart/form-data' in content_type:
            data = req.form.to_dict()
        else:
            data = dict()
    except Exception:
        traceback.print_exc()
        data = dict()
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scripts/<path:path>')
def scripts(path):
    return render_template(path, HOST=HOST, PORT=PORT)


@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('./styles', 'index.css')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./static', 'favicon.ico')


@app.route('/update_record', methods=['POST'])
def update_record():
    data = parse_reqdata(requests)
    record_time = data.get('record_time')
    CH01 = data.get('CH01')
    CH02 = data.get('CH02')
    CH03 = data.get('CH03')
    CH04 = data.get('CH04')
    print(record_time, CH01, CH02, CH03, CH04)

    output = dict()
    output['message'] = 'server received'
    return output


@socketio.on('connect_response')
def connect_response(reqdata):
    print('connected', reqdata.get('msg', ''))


@socketio.on('check_temp')
def check_temp(reqdata):
    data = {
        'record_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        'CH01': randint(40, 70),
        'CH02': randint(40, 70),
        'CH03': randint(40, 70),
        'CH04': randint(40, 70)
        }
    emit('temp_response', data)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port='5003', debug=True)
