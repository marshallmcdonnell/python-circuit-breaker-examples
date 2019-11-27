import requests

from circuitbreaker_flask_example.mock_server import app

def get_greeting(url, port):
    response = requests.get("http://{}:{}/".format(url, port))
    print(response.text)

if __name__ == "__main__":
    url = "localhost"
    port = 5000
    with app.run(url, port):
        get_greeting(url, port)

    get_greeting(url, port)
