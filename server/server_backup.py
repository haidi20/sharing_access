import os
import json
import jsonify
import pyodbc
import platform
import subprocess
import logging
import pandas as pd
from flask_cors import CORS
from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# CORS(app, cors=CORS(app, resources={r"/socket.io/*": {"origins": "*"}}))
# socketio = SocketIO(app, cors_allowed_origins="*")

app = Flask(__name__)
# socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

# info = subprocess.STARTUPINFO()


@app.route("/")
def index():
    return render_template("index.html")


# def ping(host):
#     output = subprocess.Popen(
#         ["ping", "-n", "1", "-w", "500", host], stdout=subprocess.PIPE, startupinfo=info
#     ).communicate()[0]

#     if "Destination host unreachable" in output.decode("utf-8"):
#         return f"{host} offline"
#     elif "Request timed out" in output.decode("utf-8"):
#         return f"{host} offline"
#     else:
#         return f"{host} ONLINE"


@socketio.on("connect")
def test_connect():
    emit("after connect", {"data": "terkoneksi"})


@socketio.on("request data")
def handle_connect():
    response = []
    # hostname = "192.168.1.12"
    cnxn = pyodbc.connect(
        # r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\TEST-PC\sharing\testing.mdb;"
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\192.168.1.12\sharing\testing.mdb;"
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

    # response = app.response_class(
    #     response=json.dumps(data), status=200, mimetype="application/json"
    # )

    emit("response data", {"data": data})


if __name__ == "__main__":
    socketio.run(app, host="localhost", debug=True)

# debug=True
