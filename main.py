from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    #下２つの書き方でEnum型を返せる
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message":"Have some residuals"}



@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    """
    パスを含んだパスパラメータを設定する。よくわからない。

    パス /files/{file_path} となる path operation を持っているとしましょう。
    ただし、 home/johndoe/myfile.txt のようなパスを含んだ file_path が必要です。
    したがって、URLは /files/home/johndoe/myfile.txt の様になります。
    
    らしい。どう使うのか例がなくてよくわからん…
    """
    return {"file_path": file_path}