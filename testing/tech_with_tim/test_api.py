import pytest
from api import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_user(client):
    response = client.post('/users', json={"id": 1, "name": "Alice"})
    
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Alice"}


def test_get_user(client):
    client.post('/users', json={"id": 2, "name": "Bob"})
    response = client.get('/users/2')
    
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Bob"}


def test_get_user_not_found(client):
    response = client.get('/users/99')
    
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}


def test_add_duplicate_user(client):
    client.post('/users', json={"id": 3, "name": "Charlie"})
    response = client.post('/users', json={"id": 3, "name": "Charlie"})

    assert response.status_code == 400