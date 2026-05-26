# STORING DATA

# JSON FORMAT

# json.dumps() function
# takes data, that should be converted to json
# returns string

# json.loads() function
# takes json formated string
# returns python object (any)



# SAVING AND READING

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

# write
BASE = Path(__file__).parent
path = Path(BASE/"numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
print()

# read
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
print()



'''
username = input("What is your name? ")

# write
BASE = Path(__file__).parent
path = Path(BASE/"username.json")
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")
print()

# read
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username}")
print()
'''


# exists() method
# return True if file or folder exists

BASE = Path(__file__).parent
path = Path(BASE/"username.json")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
print()
