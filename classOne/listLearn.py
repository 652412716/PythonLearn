"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[-1])

print(bicycles)

bicycles[0] = 'aimingChen'
print(bicycles)

bicycles.append('fixBox')
print(bicycles)


bicycles.insert(0, 'google')
print(bicycles)

del bicycles[0]
print(bicycles)



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")
"""


cars = ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars, reverse=True))
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars.reverse()
print(cars)

print(len(cars))

for car in cars:
    print(car)

# range创建数字列表
for value in range(1, 5):
    print("value = ", value)

numbers = list(range(10, 21))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)


print(min(squares))
print(max(squares))
print(sum(squares))


squares = [value**2 for value in range(2, 13, 2)]
print(squares)

players = ['aimingChen', 'Fish', 'Justin', 'eil', 'michael']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-2])


for player in players[:3]:
    print(player)

my_food = ["pizza", "coke", "cake"]
friend_food = my_food[1:]

my_food.append("rice")
friend_food.append("iceCream")
print(friend_food)








