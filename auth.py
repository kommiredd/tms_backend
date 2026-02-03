from fastapi import APIRouter, HTTPException
from database import users
from models import Register, Login
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: Register):
    print("Register API called")
    if users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    pwd = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode
    users.insert_one({
        "name": user.name,
        "email": user.email,
        "password": pwd,
        "role": "USER"
    })
    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: Login):
    db_user = users.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user['password'].encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "user_id": str(db_user["_id"]),
        "email": db_user["email"],
        "role": db_user["role"]
    }
