"""
Annotated + Depends example

fastapi dev ch3/03_annotated.py
"""

from typing import Annotated
from fastapi import FastAPI, Depends, Query

app = FastAPI()

def get_pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(20, ge=1, le=100)
):
    return {"skip": skip, "limit": limit}

PaginationDep = Annotated[dict, Depends(get_pagination)]

@app.get("/items/")
async def read_items(pagination: PaginationDep):
    return pagination

@app.get("/users")
async def read_users(pagination: PaginationDep):
    return pagination
