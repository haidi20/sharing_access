import os
import socket
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    container_name = "server"
    ip = "192.168.1.12"
    container_port = "5000"
    # Use the ping command to check if the container is reachable
    ping = subprocess.run(
        ["ping", "-c", "3", "-w", "3", container_name, ":", container_port],
        # ["ping", "-c", "3", "-w", "3", ip],
        capture_output=True,
        text=True,
    )

    # Check the return code
    if ping.returncode == 0:
        return f"{container_name} is reachable"
    else:
        return f"{container_name} is not reachable"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
