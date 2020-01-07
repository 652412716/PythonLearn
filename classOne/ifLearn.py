cars = ["audi", "bmw", "toyota", "honda"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

if "bmw" in cars:
    print("I have BMW!")

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

