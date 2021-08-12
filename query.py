from fastapi import FastAPI

app = FastAPI()

fake_items_db  = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    クエリパラメータは固定パスではない。デフォルト値を持つだけ。
    http://127.0.0.1:8000/items/?skip=20　にアクセスすると関数内のパラメータは
    skip=20,limit=10になる。ふむ。
    """
    return fake_items_db[skip : skip + limit]

