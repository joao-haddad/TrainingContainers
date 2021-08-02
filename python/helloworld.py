from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from " + socket.gethostname()

app.run(host='0.0.0.0', port=8080)
