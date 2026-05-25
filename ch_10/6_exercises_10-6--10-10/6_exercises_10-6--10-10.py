# 10-6
a = input("First number: ")
b = input("Second number: ")
try:
    print(f"Sum: {int(a) + int(b)}")
except ValueError:
    print("Frist and second inputs should be numbers.")
print()

# 10-7
print("Enter two number to get their sum.")
print("To finish enter 'q'.")
while True:
    a = input("First number: ")
    if a == "q": 
        break
    b = input("Second number: ")
    if b == "q":
        break
    try:
        sum = int(a) + int(b)
    except ValueError:
        print("Frist and second inputs should be numbers.")
    else:
        print(f"Sum: {sum}")
        print()
print()

# 10-8
from pathlib import Path
BASE = Path(__file__).parent
def readfile(filename):
    path = Path(BASE/filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        #print(f"File {filename} doesn't exist")
        pass
    else:
        lines = contents.split()
        print(lines)
readfile("cats.txt")
readfile("dogs.txt")
print()

# 10-9
# +

# 10-10
path = Path(BASE/"white_fang.txt")
contents = path.read_text()
print(contents.count("the"))
print(contents.lower().count("the"))
print(contents.lower().count("the "))
print(contents.lower().count(" the"))
print(contents.lower().count(" the "))
print()
