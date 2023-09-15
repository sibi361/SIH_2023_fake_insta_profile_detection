import model

model.setupModel()

fake = [0, 0, 0, 0, 0, 0, 9, 0]
real = [1, 0, 0, 0, 1, 5, 866, 953]
real2 = [1, 0, 37, 0, 0, 1, 97, 141]

current = fake
current = real
# current = real2

print(model.predict(current))
