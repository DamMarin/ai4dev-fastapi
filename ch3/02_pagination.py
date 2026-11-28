"""
Pagination Dependency

fastapi dev ch3/02_pagination.py
"""

from fastapi import FastAPI, Depends, Query

app = FastAPI()

def get_pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(20, ge=1, le=100)
):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(pagination: dict = Depends(get_pagination)):
    return pagination

@app.get("/users/")
async def read_users(pagination: dict = Depends(get_pagination)):
    return pagination

# @app.get("/products/")
# async def read_products(skip: int = 0, limit: int = 100):
#     pagination = {"skip": skip, "limit": limit}
#     return pagination
