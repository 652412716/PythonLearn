alien_0 = {"color": "green", "point": 5}
print(alien_0["color"])
print(alien_0["point"])

alien_0["speed"] = 5
print(alien_0)

# del alien_0["point"]
# print(alien_0)

for key, value in alien_0.items():
    print("key = ", key)
    print("value = ", value)

for key in alien_0.keys():
    print(key)
print("-------------")

for key in alien_0:
    print(key)
print("-------------")

for value in alien_0:
    print(value)
print("-------------")

for value in alien_0.values():
    print(value)




