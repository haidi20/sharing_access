from socketIO_client import SocketIO, LoggingNamespace


def onConnect():
    print("connect")


def onAfterConnect(*args):
    print(args)


socketIO = SocketIO("localhost", 5000, LoggingNamespace)
socketIO.emit("connect", onConnect)

socketIO.on("after_connect", onAfterConnect)
socketIO.wait(seconds=1)
