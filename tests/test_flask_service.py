import pytest

from circuitbreaker_flask_example.flask_service import app

def test_index():
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert response.status_code == 200
    assert response.data == b'Welcome to the Flask App!'
    

def test_greetings():
    tester = app.test_client()
    response = tester.get('/greetings', content_type='html/text')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

