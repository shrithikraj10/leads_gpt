from fastapi import APIRouter, HTTPException
from app.schemas.auth import UserLogin, UserSignup

router = APIRouter()

# Mock user storage
users_db = {}

@router.post("/signup")
def signup(user: UserSignup):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.email] = user
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    if user.email not in users_db or users_db[user.email].password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": "mock-jwt-token"}
