# DIFFERENT IF STATEMENTS



# SIMPLE IF

# if (conditional_test):
#	(do_something)

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print()



# IF-ELSE STATEMENTS

# if (conditional_test):
#	(do_something)
# else:
#	(do_something_else)

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print()



# IF-ELIF-ELSE CHAIN

# if (conditional_test_1):
#	(do_something_1)
# elif (conditional_test_2):
# 	(do_something_2)
# else:
#	(do_something_else)
#! only 1 condition could be True

age = 12
if age < 4:
    price = 0
elif age < 18:
	price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
print()

#! not 1 but many ELIF can be used

#! ELSE block is NOT necessary in the end



# SERIES OF SIMPLE IF STATEMENTS

# if (conditional_test_1):
#	(do_something_1)
# if (conditional_test_2):
#	(do_something_2)
#! more than 1 condition could be True

requested_toppings = ["mashrooms", "extra cheese"]

if "mashrooms" in requested_toppings:
    print("Adding mashrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")

