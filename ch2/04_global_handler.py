"""
Global Exception Handler

fastapi dev ch2/04_global_handler.py
"""
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(
        "Unhandled error on %s %s",
        request.method,
        request.url.path,
        exc_info=exc,
    )
    return JSONResponse(
        status_code=500,
        content={"detail ": "Internal Server Error"},
    )

users = {1: "George", 2: "Maria"}
items = {1: "Laptop", 2: "Mouse"}

# call Exception
@app.get("/crash")
async def crash():
    raise ValueError(f"Just crashed")

# HTTPException
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": items[item_id]}

# Shows bug on logger
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": users[user_id]}