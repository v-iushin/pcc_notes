# IF WITH LISTS

requested_toppings = ["mashrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
print()



# CHECKING THAT A LIST IS NOT EMPTY

#! if (empty_list)	False
#! if (list)		True

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")