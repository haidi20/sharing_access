import json
import pyodbc
import pandas as pd
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\TEST-PC\sharing\testing.mdb;')

    df = pd.read_sql("SELECT TOP 1 * FROM campaign_table ct ORDER BY ID DESC", cnxn) 
    
    # print(df.head())
    
    data = df.to_json(orient='records')
    
    if(type(data) == str):
        return json.loads(data)
    else:
        return "not"
    
@socketio.on('connect')
def test_connect():
    emit('after connect', {'data': 'terkoneksi'})

if __name__ == '__main__':
    socketio.run(app, host='localhost', debug=True)