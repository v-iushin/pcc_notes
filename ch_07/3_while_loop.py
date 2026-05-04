# WHILE LOOP

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()

promt = "Tell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(promt)
    if message != "quit":
        print(message)
print()

