from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    user = {
        "name": "John Doe",
        "age": 20,
        "score": 100.0
    }
    response = client.post("/user/", json=user)
    assert response.status_code == 200
    assert response.json() == user


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200

    users = [
        {
            "name": "John Doe",
            "age": 20,
            "score": 100.0
        },
        {
            "name": "Mary Doe",
            "age": 19,
            "score": 100.0
        },
        {
            "name": "Anna Thomas",
            "age": 19,
            "score": 100.0
        }
    ]
    assert response.json() == users
