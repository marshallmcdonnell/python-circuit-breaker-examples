import pytest
import requests
from python_circuit_breaker_examples import client_circuitbreaker, mock_server

url = "localhost"
port = 5000

def test_get_greeting():
    ''' Test for server respnse to client is correct '''
    with mock_server.app.run(url, port):
        response = client_circuitbreaker.get_greeting(url, port)
        assert response == "Hello world!"

def test_get_greeting_failure():
    ''' Test an exception is raised when the server is not running '''
    with pytest.raises(requests.exceptions.ConnectionError):
        client_circuitbreaker.get_greeting(url, port)
