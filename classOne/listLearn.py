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

"""

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



