"""
Path Operation Configuration

fastapi dev ch13/05_path_operation_config.py
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post(
    "/items/",
    tags=["items"],
    summary="Create a new item",
    description="Creates an item",
    status_code=status.HTTP_201_CREATED,
    response_description="A new item",
    responses={
        404: {"description": "Not found"},
        422: {"description": "Validation Error"}
              },
)
async def create_item(item: Item):
    return {"id": 1, "name": item.name, "price": item.price}
