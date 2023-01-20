import json
from socketIO_client import SocketIO, LoggingNamespace


def onConnect():
    return True
    # print("connect")


def onAfterConnect(*args):
    responses = json.dumps(args)
    responses = json.loads(responses)

    for item in responses[0]["data"]:
        print(item["First_Name"])


socketIO = SocketIO("localhost", 5000, LoggingNamespace)
socketIO.emit("request_data")

socketIO.on("response_data", onAfterConnect)
socketIO.wait(seconds=0.1)
