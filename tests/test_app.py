import pytest

from app import app


def test_greetings():
    tester = app.test_client()
    response = tester.get('/greetings', content_type='html/text')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

