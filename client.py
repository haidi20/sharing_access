import socketio

sio = socketio.Client()

@sio.on('after connect')
def on_message(data):
    print(data)

sio.connect('http://localhost:5000')
sio.wait()
