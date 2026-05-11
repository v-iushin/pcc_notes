# ARBITRARY NUMBER OF ARGUMENTS

# func(*PARAM)
# (*PARAM) means to make a TUPLE 
# called PARAM, containing all values

def make_pizza(*toppings):
    """Summaraize the pizza we are about to make."""
    print("Making pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mashrooms", "green pepper", "extra cheese")
print()



# POSITIONAL AND ARBITRARY ARGUMENTS

def make_pizza(size, *toppings):
    """Summaraize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mashrooms", "green pepper", "extra cheese")
print()



# ARBITRARY KEYWORD ARGUMENTS

# func(**PARAM)
# (**PARAM) means to make a DICTIONARY 
# called PARAM, containing all key-values

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info
user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics")
print(user_profile)
print()
