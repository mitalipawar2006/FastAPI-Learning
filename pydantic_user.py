from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


app = FastAPI()


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, gt=0, le=120)


fake_users_db = []


@app.post("/users/")
async def create_user(user: User):
    fake_users_db.append(user.model_dump())

    return {
        "message": "User created successfully",
        "user": user
    }


@app.get("/users/")
async def get_users():
    return {
        "users": fake_users_db
    }