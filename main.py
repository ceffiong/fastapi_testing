from fastapi import FastAPI
from schema import User

app = FastAPI()


@app.post("/user/", response_model=User)
async def create_user(user: User):
    return user


@app.get("/users/", response_model=list[User])
async def get_users():
    return [
        User(name="John Doe", age=20, score=100.0),
        User(name="Mary Doe", age=19, score=100.0),
        User(name="Anna Thomas", age=19, score=100.0),
    ]