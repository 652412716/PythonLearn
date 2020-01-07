def greet_user(username):
    print("Hello," + username.title() + "!")


greet_user("aimingChen")


def make_pizza(*toppings):
    print(toppings)
    print(type(toppings))


make_pizza("apple")
make_pizza("apple", "orange")




