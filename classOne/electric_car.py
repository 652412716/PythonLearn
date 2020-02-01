class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_size = 100

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car has a " + str(self.gas_tank_size) + "L gas tank.")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_distance(self):
        if self.battery_size == 70:
            distance = 240
        elif self.battery_size == 85:
            distance = 270

        message = "This car can go approximately " + str(distance)
        message += " miles on fill charge."
        print(message)


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()
        self.gas_tank_size = 0

    def fill_gas_tank(self):
        print("Electric car doesn't need a gas tank.")


my_tesla = ElectricCar('tesla', 'model 3', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.fill_gas_tank()
print(my_tesla.gas_tank_size)
my_tesla.battery_size.get_distance()
