from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    user = {
        "name": "John Doe",
        "age": 20,
        "score": 100
    }
    response = client.post("/user/", json=user)
    assert response.status_code == 200
    assert response.json() == user


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200

    users = [
        {
            "name": "John Does",
            "age": 20,
            "score": 100
        },
        {
            "name": "Mary Doe",
            "age": 19,
            "score": 100
        },
        {
            "name": "Anna Thomass",
            "age": 19,
            "score": 100
        }
    ]
    assert response.json() == users
