from model.model import *
import fastapi


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

app = fastapi.FastAPI()


@app.post("/predict")
def pred(profile_pic, name_same_username, description_length,
         external_url, private, posts, followers, follows):
    output = say(predict([1]))
    return {"result": output}


@app.get("/")
def showHome():
    