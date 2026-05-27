# 10-11
from pathlib import Path
import json
#
BASE = Path(__file__).parent
path = Path(BASE/"favorite_number.json")
#
fav_num = input("What is your favorite number? ")
contents = json.dumps(fav_num)
path.write_text(contents)
print()
#
contents = path.read_text()
fav_num = json.loads(contents)
print(f"I know your favorite number! It's {fav_num}.")
print()

# 10-12
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number! It's {fav_num}.")
else:
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
print()

# 10-13
def get_stored_user(path):
    """Get stored user's info if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None
def get_new_user(path):
    """Prompt for a new user's info."""
    user = {}
    user["name"] = input("What is your name? ")
    user["age"] = input("What is your age? ")
    user["gender"] = input("What is your gender? ")
    contents = json.dumps(user)
    path.write_text(contents)
    return user
def greet_user1():
    """Greet the user."""
    BASE = Path(__file__).parent
    path = Path(BASE/"user.json")
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user["name"]}!")
        print(f"Your age is {user["age"]}, you are {user["gender"]}.")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you came back, {user["name"]}!")
greet_user1()
print()

# 10-14
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user2():
    """Greet the user by name."""
    BASE = Path(__file__).parent
    path = Path(BASE/"username.json")
    username = get_stored_username(path)
    if username:
        ans = input(f"Are you {username}? (y/n) ")
        if ans == "y":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you came back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you came back, {username}!")
greet_user2()
print()
