from fastapi import FastAPI, Depends

app = FastAPI()

def get_query(q: str | None = None):
    if q:
        return q.strip().lower()
    return q

@app.get("/items/")
async def read_items(q: str | None = Depends(get_query)):
    return {"q": q}