# BREAK STATEMENT

# BREAK quits ANY LOOP
#! only one level
promt = "Please enter the name of a citi you have visited:"
promt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(promt)
    if city == "quit":
        break
    else:
        print(f"I would love to go to {city.title()}!")
print()



# CONTINUE STATMENT

# CONTINUE returns begining of ANY LOOP
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print()
