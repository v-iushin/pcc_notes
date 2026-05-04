# MULTIPLE LISTS

available_toppings = ["mashrooms", "olives",
                      "green peppers", "pepperoni",
                      "pineapple", "extra cheese"]
requested_toppings = ["mashrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making pizza!")

