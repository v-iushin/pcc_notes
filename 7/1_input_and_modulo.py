# INPUT() FUNCTION

# INPUT(PROMT) returns string

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print()

# CONCATENATION
#
# a += b
# ->
# a = a + b 
#
# JOIN()
# words_list = [...]
# result = "".join(words_list)
promt = "If you share your name, we can personalize the message you see."
promt += "\nWhat is your first name? "
name = input(promt)
print(f"Hello, {name}!")
print()

# INT() function converts to integer to farther comparation
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("You are tall enough to ride!")
else:
    print("You will be able to ride when you are a little older.")
print()



# MODULO OPERATOR 
# %

# A % B
# divides A by B and returns remainder
#
# 4 % 3 = 1

number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even.")
else: 
    print(f"The number {number} is odd.")



