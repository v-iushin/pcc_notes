# 8-12
def make_sandwich(*items):
    print("You made sandwich with:")
    for item in items:
        print(f"- {item}")
make_sandwich("1")
make_sandwich("1", "2")
make_sandwich("1", "2", "3")
print()

# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info
user_profile = build_profile("FIRST", "LAST",
                             location="LOCATION",
                             field="FIELD",
                             language="PYTHON")
print(user_profile)
print()

# 8-14
def make_car(manuf, model, **info):
    info["manuf"] = manuf
    info["model"] = model
    return info
car = make_car("subaru", "outback", 
               color="blue", 
               tow_package=True)
print(car)
print()
