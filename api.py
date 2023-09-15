from model import model
from typing import Annotated
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
# from fastapi.encoders import jsonable_encoder


def say(output):
    if (output):
        print("fake")
        return "fake"
    else:
        print("not fake")
        return "not fake"


model.setupModel()

app = FastAPI()
api = FastAPI()
app.mount("/api", api, name="api")
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@api.post("/v1/predict")
async def predict(request: Request):
    formData = await request.form()
    # formData = jsonable_encoder(formData)
    # print(formData)
    # print(list(formData.values()))
    # return formData

    output = say(model.predict(list(formData.values())))
    print(output)
    return {"result": output}
