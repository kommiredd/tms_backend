import bcrypt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ticket_management"]
users = db["users"]

hashed = bcrypt.hashpw("test123".encode(), bcrypt.gensalt()).decode()

users.update_one(
    {"email": "user@example.com"},
    {"$set": {"password": hashed}}
)

print("Password reset to test123")
