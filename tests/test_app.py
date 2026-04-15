import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_home_page(client):
    """Test if homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200


def test_prediction_route(client):
    """Test prediction with sample text"""
    response = client.post('/', data={
        "news": "Government announces new policy for economic growth"
    })
    assert response.status_code == 200


def test_fake_news_sample(client):
    """Test fake news input"""
    response = client.post('/', data={
        "news": "Breaking!!! Secret formula to become rich overnight!!!"
    })
    assert response.status_code == 200