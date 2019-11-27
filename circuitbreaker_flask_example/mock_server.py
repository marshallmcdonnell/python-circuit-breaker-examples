from http_server_mock import HttpServerMock
import requests

app = HttpServerMock(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello world!"

