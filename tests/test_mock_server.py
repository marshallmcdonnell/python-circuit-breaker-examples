import pytest
import requests

from circuitbreaker_flask_example.mock_server import app

def test_index():
    with app.run("localhost", 5000):
        response = requests.get("http://localhost:5000/")
        assert response.status_code == 200
        assert response.text == "Hello world!"

