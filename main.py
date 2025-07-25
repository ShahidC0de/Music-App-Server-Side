from fastapi import FastAPI, Request
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

app = FastAPI()
@app.post("/signup")
def user_signup(user: UserCreate):
    print(user.name)
    print(user.email)
    print(user.password)

