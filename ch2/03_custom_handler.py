"""
Custom Handler


"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = { 1: "Laptop", 2: "Mouse" }


class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

def get_item(item_id: int) -> str:
    if item_id not in items:
        raise ItemNotFoundError(item_id)
    return items[item_id]

@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": get_item(item_id)}