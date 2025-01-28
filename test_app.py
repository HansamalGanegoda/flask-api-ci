# test_app.py
import pytest
from app import app

# Test case for the /add endpoint
def test_add():
    client = app.test_client()
    response = client.get('/add')
    assert response.status_code == 200
    assert response.json == {'result': 5}

# Test case for the /subtract endpoint
def test_subtract():
    client = app.test_client()
    response = client.get('/subtract')
    assert response.status_code == 200
    assert response.json == {'result': 2}
