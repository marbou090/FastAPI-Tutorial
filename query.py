from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str]= None, short: bool= False):
    """
    関数パラメータ q はオプショナルとなり、デフォルトでは None 
    この場合、以下にアクセスすると:
    http://127.0.0.1:8000/items/foo?short=1
    もしくは、
    http://127.0.0.1:8000/items/foo?short=True
    もしくは、
    http://127.0.0.1:8000/items/foo?short=true
    もしくは、
    http://127.0.0.1:8000/items/foo?short=on
    もしくは、
    http://127.0.0.1:8000/items/foo?short=yes

    http://127.0.0.1:8000/items/maru?short=1&q=hoge&short=False
    だと
    {"item_id":"maru","q":"hoge","description":"This is an amazing item that has a long description"}
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item