# 7-1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")
print()

# 7-2
dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
print()

# 7-3
number = input("Write a number: ")
number = int(number)
if number % 10 == 0:
    print(f"Number {number} IS a multiple of 10.")
else:
    print(f"Number {number} IS NOT a multiple of 10.")

