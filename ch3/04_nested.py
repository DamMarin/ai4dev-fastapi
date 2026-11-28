"""
Nested Dependecies


"""

from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

fake_users = {
    "john-token": {"username": "john", "active": True},
    "maria-token": {"username": "maria", "active": False},
}

def get_current_user(
      token: Annotated[str | None, Header(alias="X-Token")] = None
):
    if token not in fake_users:
        raise HTTPException(status_code=401, detail="Invalid token")
    return fake_users[token]

def get_current_active_user(
        user: Annotated[dict, Depends(get_current_user)]
):
    if not user["active"]:
        raise HTTPException(status_code=403, detail="Inactive user")
    return user

@app.get("/me")
async def read_me(user: Annotated[dict, Depends(get_current_active_user)]):
    return user
