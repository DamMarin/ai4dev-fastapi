"""
Validation with Path and Query Parameters

fastapi dev ch13/04_validation.py
"""

from fastapi import FastAPI, Path, Query, HTTPException
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
        item_id: Annotated[int, Path(ge=0, description="The Item ID")],
        q: Annotated[str | None, Query(
            min_length=1,
            max_length=3,
            description="The query parameter"
        )] = None,
        limit: Annotated[int, Query(
            ge=1,
            description="The maximum number of items to return"
        )] = 10,
):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not Found")

    return {"item_id": item_id, "q": q}