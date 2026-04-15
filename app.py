import pytest
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_prediction(client):
    response = client.post('/', data={
        "news": "Government announces new policy"
    })
    assert response.status_code == 200