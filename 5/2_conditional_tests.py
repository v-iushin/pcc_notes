# CONDITIONAL TESTS

#! ONLY True and False are booleans
#! true and false (lowercase) are NOT



# EQUALITY
# == is equality operator

car = "bmw"
print(car == "bmw")		# True
print(car == "audi")	# False

print(car == "BMW")		# False
# case is important

car = "Audi"
print(car.lower() == "audi")	# True
print(car)
# doesnt change the variable
print()



# INEQUALITY
# != inequality operator

requested_topping = "mashroom"
if requested_topping != "anchovies":
    print("Hold the anchovies!")
print()



# NUMERICAL COMPARATIONS
# ... other operators

age = 21
print(age == 21)	# True
print(age != 21)	# False
print(age < 21)		# False
print(age <= 21)	# True
print(age > 21)		# False
print(age >= 21)	# True