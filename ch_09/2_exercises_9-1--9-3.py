# 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is open")
restaurant1 = Restaurant("1-1", "1-2")
print(f"{restaurant1.restaurant_name}")
print(f"{restaurant1.cuisine_type}")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print()

# 9-2
restaurant2 = Restaurant("2-1", "2-2")
restaurant3 = Restaurant("3-1", "3-2")
restaurant4 = Restaurant("4-1", "4-2")
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()
print()

# 9-3
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
user1 = User("a1", "b1", 1, "c1")
user2 = User("a2","b2", 2, "c2")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
print()