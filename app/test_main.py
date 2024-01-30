# test for file main.py
import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}