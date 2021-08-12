from fastapi import FastAPI

app = FastAPI()

fake_items_db  = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str]= None):
    """
    関数パラメータ q はオプショナルとなり、デフォルトでは None 
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}