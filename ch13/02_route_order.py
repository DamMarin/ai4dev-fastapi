"""
Route Order

fastapi dev ch13/02_route_order.py
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def get_user_me():
    return {"username": "me!"}

@app.get("/users/{username}")
async def get_username(username):
    return {"username": username}

