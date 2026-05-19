from user_9_12 import User

class Privileges:
    def __init__(self, *privileges: str):
        self.privileges = list(privileges)
    def show_privileges(self):
        print(f"Privilieges: {self.privileges}")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender): #, *privileges: str):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges("1", "2", "3")