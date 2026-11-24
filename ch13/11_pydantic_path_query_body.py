"""
Path, Query & Body
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item,
        q: str | None = None,
):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result["q"] = q
    return result
