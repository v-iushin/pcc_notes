# EXCEPTIONS



# ZeroDivisionError
# ValueError

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print()

print("Give me two numbers, and I'll devide them.")
print("Enter 'q' to quit.")

#! any code that executed successfully 
#! in TRY block goes to ELSE block

while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("First and second input should be numbers")
    else:
        print(answer)
    print()
print()



# FileNotFoundError

#! split() method split string 
#! when finds any whitespace
#! return list

from pathlib import Path

def count_words(path, file):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
        #pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file} has about {num_words} words.")

BASE = Path(__file__).parent
filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for filename in filenames:
    path = Path(BASE/filename)
    count_words(path, filename)
print()

# FAILING SILENTLY
# it possible to tell python to do nothing
# in the EXCEPT block
# instead of code just write PASS
