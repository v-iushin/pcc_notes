# IN OR NOT IN THE LIST

# (...value) in (...list)
requested_toppings = ["mashrooms", "onions", "pineapples"]
print("mashrooms" in requested_toppings)	# True
print("pepperoni" in requested_toppings)	# False
print()


# (...value) not in (...list)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

