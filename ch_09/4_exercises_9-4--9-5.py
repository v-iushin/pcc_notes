# 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment):
        self.number_served += increment
restaurant = Restaurant("1-1", "1-2")
print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Customers served: {restaurant.number_served}")
restaurant.set_number_served(10)
print(f"Customers served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Customers served: {restaurant.number_served}")
print()

# 9-5
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    def greet_user(self):
        print(f"Hey, {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_loging_attempts(self):
        self.login_attempts = 0
user = User("a1", "b1", 1, "c1")
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_loging_attempts()
print(user.login_attempts)
print()
