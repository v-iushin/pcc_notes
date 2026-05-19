class Privileges:
    def __init__(self, *privileges: str):
        self.privileges = list(privileges)
    def show_privileges(self):
        print(f"Privilieges: {self.privileges}")

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