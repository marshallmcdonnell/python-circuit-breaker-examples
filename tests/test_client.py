
from circuitbreaker_flask_example import client, mock_server

url = "localhost"
port = 5000

def test_get_greeting():
    with mock_server.app.run(url, port):
        response = client.get_greeting(url, port)
        assert response == "Hello world!"
