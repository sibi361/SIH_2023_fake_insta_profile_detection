from oldModel.model import *
import fastapi


def say(output):
    if (output):
        print("fake")
    else:
        print("not fake")


setupModel()
# fake = ["9876543", 0, 9, 0, 1, 0, 0]
# real = ["2312313", 2, 866, 953, 1, 282, 5]

# output = predict(fake)
# say(output)

# output = predict(real)
# say(output)

app = fastapi.FastAPI()

@app.get("/")
def pred(statuses_count,followers_count,friends_count,favourites_count):
    