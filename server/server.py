import json
import pyodbc
import pandas as pd
from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")


@socketio.on("connect")
def test_connect():
    emit("after connect", {"data": "connected"})


@socketio.on("request_data")
def handle_connect():
    response = []
    cnxn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\TEST-PC\sharing\testing.mdb;"
        # r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\192.168.1.12\sharing\testing.mdb;"
    )

    df = pd.read_sql("SELECT TOP 10 * FROM campaign_table ct ORDER BY ID DESC", cnxn)
    data = df.to_json(orient="records")
    data = json.loads(data)
    for i in range(len(data)):
        date_added = data[i]["Date_Added"]
        date_added = datetime.fromtimestamp(date_added / 1000).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        data[i]["Date_Added"] = date_added

    emit("response_data", {"data": data})


if __name__ == "__main__":
    socketio.run(app, host="localhost", debug=True)
