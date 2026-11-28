"""
HTTPException headers

fastapi dev ch2/02_http_exception_headers.py
"""
from typing import Annotated

from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

VALID_TOKEN = "secret"

@app.get("/protected")
async def protected(
        authorization:  Annotated[str | None, Header()]
):
    if authorization != f"Bearer {VALID_TOKEN}":
        print(authorization)
        raise HTTPException(
          status_code=401,
          detail={
              "code": "NOT_AUTHENTICATED",
              "message": "Unauthorized"
          },
          headers={"WWW-Authenticate": "Bearer"}
        )
    return {"message": "Welcome AI4DEV"}

# works only with
# curl -i http://localhost:8000/protected -H "Authorization: Bearer secret"