# 9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = list(flavors)
    def show_flavors(self):
        print(f"Flavors: {self.flavors}")
ice_rest = IceCreamStand("NAME", "CUISINE", "1", "2", "3")
ice_rest.show_flavors()
print()

# 9-8
class Privileges:
    def __init__(self, *privileges: str):
        self.privileges = list(privileges)
    def show_privileges(self):
        print(f"Privilieges: {self.privileges}")

# 9-7
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    def greet_user(self):
        print(f"Hey, {self.first_name} {self.last_name}")
class Admin(User):
    def __init__(self, first_name, last_name, age, gender): #, *privileges: str):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges("1", "2", "3")
    #    self.privileges = list(privileges)
    #def show_privileges(self):
    #    print(f"Privilieges: {self.privileges}")
#admin = Admin("a", "b", 1, "m", "1", "2", "3")
admin = Admin("a", "b", 1, "m")
#admin.show_privileges()
admin.privileges.show_privileges()
print()

# 9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def uptade_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("Filling gas tank.")
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")
e_car = ElectricCar("nissan", "leaf", 2024)
print(e_car.get_descriptive_name())
e_car.battery.describe_battery()
e_car.battery.get_range()
e_car.battery.upgrade_battery()
e_car.battery.describe_battery()
e_car.battery.get_range()
print()
