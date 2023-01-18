import pyodbc
import logging
import pandas as pd
from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    response = []
    cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\TEST-PC\sharing\testing.mdb;')

    df = pd.read_sql("SELECT TOP 10 Date_Added FROM campaign_table ct ORDER BY ID DESC", cnxn) 
    data = df.to_json(orient='records')
    data = json.loads(data)
    for i in range(len(data)):
        date_added = data[i]['Date_Added']
        date_added = datetime.fromtimestamp(date_added/1000).strftime('%Y-%m-%d %H:%M:%S')
        data[i]['Date_Added'] = date_added
    
    emit('after connect', {'data': data})

if __name__ == '__main__':
    socketio.run(app)