from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")


@socketio.on("connect")
def test_connect():
    emit("after_connect", {"data": "terkoneksi"})


if __name__ == "__main__":
    socketio.run(app, host="localhost", debug=True)
