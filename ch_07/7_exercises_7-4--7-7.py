# 7-4
pizza_topping = []
mes = "Write pizza toppping. Write 'quit' to finish.\n"
while True:
    p_t = input(mes)
    if p_t == "quit":
        break
    else:
        pizza_topping.append(p_t)
print(f"You will add: {", ".join(pizza_topping)}")
print()

# 7-5
mes = "Tell me age, I will tell you the ticket price."
mes += "\nWrite '-1' to finish.\n"
while True:
    age = int(input(mes))
    if age == -1:
        break
    elif age < 3:
        print("Ticket is free")
    elif 3 <= age <= 12:
        print("Price is $10")
    else:
        print("Price if $15")
print()

# 7-6(1)
pizza_topping = []
mes = "Write pizza toppping. Write 'quit' to finish.\n"
a = 0
while a != -1:
    p_t = input(mes)
    if p_t == "quit":
        a = -1
    else:
        pizza_topping.append(p_t)
print(f"You will add: {", ".join(pizza_topping)}")
print()

# 7-6(2)
pizza_topping = []
mes = "Write pizza toppping. Write 'quit' to finish.\n"
active = True
while active:
    p_t = input(mes)
    if p_t == "quit":
        active = False
    else:
        pizza_topping.append(p_t)
print(f"You will add: {", ".join(pizza_topping)}")
print()

# 7-7
while True:
    print()
