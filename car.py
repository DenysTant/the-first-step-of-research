from pathlib import Path
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

car["color"] = "white"
for name, value in car.items():
    print(name, value)

a = '\#'
if a != 0:
    print(a)

points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}

points[4] = 's'
points[(3, 3)] = 's'
print(points)


p = Path()  # p Вказує на папку з якої був запущений Python
print(p)
print(type(p))
