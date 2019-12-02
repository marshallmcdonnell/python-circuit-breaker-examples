import pytest
import requests

from python_circuit_breaker_examples.mock_server import app

def test_index():
    ''' Test to ensure the mock server index page gives correct response '''
    with app.run("localhost", 5000):
        response = requests.get("http://localhost:5000/")
        assert response.status_code == 200
        assert response.text == "Hello world!"

