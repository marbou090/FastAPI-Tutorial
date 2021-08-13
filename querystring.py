from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None, title="Query string", min_length=3,
        description="ここにたくさんせつめいかいていくぞぉ"
        )
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results