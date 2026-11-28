"""
Router level Dependencies

"""

from typing import Annotated
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header, status

app = FastAPI()

def verify_token(
        token: Annotated[str | None, Header(alias="X-Token")] = None
):
    if token != "secret":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return token


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(verify_token)],
)

@router.get("/stats")
async def get_stats():
    return {"count": 5, "total": 10}

@router.get("/items")
async def get_items():
    return ["Laptop", "Mouse"]

app.include_router(router)

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}