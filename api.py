from model.model import *
from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles


def say(output):
    if (output):
        print("fake")
    else:
        print("not fake")


setupModel()
# fake = [0, 0, 0, 0, 0, 0, 9, 0]
# real = [1, 0, 0, 0, 1, 5, 866, 953]

# output = predict(fake)
# say(output)

# output = predict(real)
# say(output)

app = FastAPI()
app.mount("/home", StaticFiles(directory="static", html=True), name="static")


@app.post("/predict")
def pred(profile_pic: Annotated[str, Form()],
         name_same_username: Annotated[str, Form()],
         description_length: Annotated[str, Form()],
         external_url: Annotated[str, Form()],
         private: Annotated[str, Form()],
         posts: Annotated[str, Form()],
         followers: Annotated[str, Form()],
         following: Annotated[str, Form()]):
    output = say(predict([profile_pic,
                          name_same_username,
                          description_length,
                          external_url,
                          private,
                          posts,
                          followers,
                          following]))
    return {"result": output}

# main site at /home
