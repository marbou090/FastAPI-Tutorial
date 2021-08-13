from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[List[str]]= Query(["foo","bar"])):
    """
    オプショナルなqはデフォルトでNone, 複数渡せる
    """
    query_items = {"q": q}
    return query_items