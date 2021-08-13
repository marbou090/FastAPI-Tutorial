from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str]= Query(None, min_length=3 ,max_length=50, regex="^fixedquery$")):
    """
    オプショナルなqはデフォルトでNone, 渡された場合は５０文字を越してはいけない
    """
    results= {"items": [{"item_id": "Foo"},{"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results