from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# root route and handle function
@app.get("/")
async def root():
    return {"message": "Hello World"}


# test route and handle function
@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"Item Id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    elif model_name is ModelName.lenet:
        return {"model_name": model_name, "message": "Have some residuals"}
    else:
        return {"message": "Not matched"}
